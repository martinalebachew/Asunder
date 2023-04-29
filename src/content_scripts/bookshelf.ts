// bookshelf.ts
// (C) Martin Alebachew, 2023

window.addEventListener("load", onUILoaded);
const download_port = chrome.runtime.connect({name: "download_port"});

function onUILoaded() {
    // A workaround for false-positive UI loaded events from Classoos.
    try {
        pinButtonToBookCovers();
    } catch (error) {
        setTimeout(onUILoaded, 200);
    }
}

function pinButtonToBookCovers() {
    const bookshelf = document.getElementsByClassName("list box-sizing")[0];
    for (const book of bookshelf.children) {
        const coverUrl = book.getElementsByTagName("img")[0].src;
        const bookId = coverUrl.split("/").pop()!.split("_")[1];

        const downloadButton = document.createElement("img");
        downloadButton.src = chrome.runtime.getURL("assets/icon-32.png");
        downloadButton.addEventListener("click", () => { downloadBookHandler(bookId); });
        book.appendChild(downloadButton);
    }
}

function downloadBookHandler(bookId: string) {
    download_port.postMessage({bookId: bookId});
}