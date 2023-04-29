// background.ts
// (C) Martin Alebachew, 2023

chrome.runtime.onConnect.addListener(function(port) {
    console.assert(port.name === "download_port");
    port.onMessage.addListener(({ bookId, token }: { bookId: string, token: string }) => {
        downloadBook(bookId, token);
    });
});