// background.ts
// (C) Martin Alebachew, 2023

let passwordToBlobB64: {[_: string]: string} = {};

chrome.runtime.onConnect.addListener((port) => {
    switch (port.name) {
        case "download_port":
            port.onMessage.addListener(({ bookId, token }: { bookId: string, token: string }) => {
                downloadBookHandler(bookId, token);
            });
            break;

        case "base64":
            port.onMessage.addListener((password: string) => {
                port.postMessage({
                    password: password,
                    blob_b64: passwordToBlobB64[password]
                });

                delete passwordToBlobB64[password];
            });
            break;

        default:
            throw `[SW ERROR] Connection on unknown port named ${port.name}.`;
    }
});

async function downloadBookHandler(bookId: string, token: string) {
    const { licenseId, userId, password } = await getLicense(bookId, token);
    const downloadUrl = await getDownloadUrl(licenseId, userId, bookId, token);
    await savePdf(downloadUrl, password, `${bookId}.pdf`);
}

async function getLicense(bookId: string, token: string) {
    const response = await (await fetch(`https://my.classoos.com/rest_api.php/books/${bookId}/license`, {
        method: "GET",
        headers: {
            Authorization: "Bearer " + token
        }
    })).json();

    const license = response.data[0];
    const licenseId = license.license_id;
    const userId = license.user_id;
    const password = license.password;
    return { licenseId, userId, password };
}

async function getDownloadUrl(licenseId: string, userId: string, bookId: string, token: string) {
    const response = await (await fetch(`https://dwb.classoos.com/api/books?LicenseID=${licenseId}&UserID=${userId}&BookID=${bookId}`, {
        method: "GET",
        headers: {
            Authorization: "Bearer " + token
        }
    })).json();

    if (!response.Success) throw `[PDF URL ERR] API denied access with message ${response.ErrorMessage} (Code ${response.ErrorCode})`;
    return response.DownloadURL;
}

async function savePdf(downloadUrl: string, password: string, filename: string) {
    const rawBlob = await (await fetch(downloadUrl, {
        method: "GET"
    })).blob();

    const pdfBlob = new Blob([rawBlob], { type: "application/pdf" });
    const b64 = await blobToBase64(pdfBlob);
    passwordToBlobB64[password] = JSON.stringify({ blob: b64 });

    // TODO: Replace with chrome.offscreen API
    await chrome.windows.create({ url: `donwloader/donwloader.html?password=${password}&filename=${filename}`, state: "minimized" });
}

function blobToBase64(blob: Blob) : Promise<string> {
    /* Modified version of
       https://stackoverflow.com/questions/18650168/convert-blob-to-base64
     */
    return new Promise((resolve, _) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result as string);
        reader.readAsDataURL(blob);
    });
}
