// background.ts
// (C) Martin Alebachew, 2023

chrome.runtime.onConnect.addListener(function(port) {
    console.assert(port.name === "download_port");
    port.onMessage.addListener(function(msg) {
        console.log(msg.bookId);
    });
});