// background.ts
// (C) Martin Alebachew, 2023

chrome.runtime.onConnect.addListener(function(port) {
    console.assert(port.name === "download_port");
    port.onMessage.addListener(({ bookId, token }: { bookId: string, token: string }) => {
        downloadBookHandler(bookId, token);
    });
});

async function downloadBookHandler(bookId: string, token: string) {
    const { licenseId, userId, password } = await getLicense(bookId, token);
    const downloadUrl = await getDownloadUrl(licenseId, userId, bookId, token);
    console.log(downloadUrl);
    // removePdfPassword(password);
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