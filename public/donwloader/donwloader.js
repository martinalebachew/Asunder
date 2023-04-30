// donwloader.js
// (C) Martin Alebachew, 2023

/* Modified version of
   https://stackoverflow.com/questions/22607150/getting-the-url-parameters-inside-the-html-page
 */

function getURLParameter(sParam) {
    const sPageURL = window.location.search.substring(1);
    const sURLVariables = sPageURL.split('&');
    for (let i = 0; i < sURLVariables.length; i++)
    {
        const sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] === sParam && sParameterName[1]) return sParameterName[1];
    }

    throw `[DOWNLOADER ERR] Failed to parse parameter ${sParam}.`
}

async function saveFile(blob) {
    await chrome.downloads.download({
        url: URL.createObjectURL(blob),
        filename: outputFilename,
    });
}


const port = chrome.runtime.connect({ name: "base64" });
const password = getURLParameter("password");
const outputFilename = getURLParameter("filename");
port.onMessage.addListener(async (message) => {
    if (message.password === password) {
        const parsed = JSON.parse(message.blob_b64);
        const blob = await fetch(parsed.blob).then(res => res.blob());
        await saveFile(blob);
        window.close();
    }
});

port.postMessage(password);