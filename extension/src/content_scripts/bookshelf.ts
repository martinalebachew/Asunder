// bookshelf.ts
// (C) Martin Alebachew, 2023

window.addEventListener("load", onUILoaded);
const download_port = chrome.runtime.connect({ name: "download_port" });
const token = localStorage["token"]; // Classoos stores session token on local storage

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
    if (book.classList.contains("book")) {
      const coverUrl = book.getElementsByTagName("img")[0].src;
      const bookId = coverUrl.match(/(?<=book_)\d+/)![0];

      const downloadButton = document.createElement("img");
      downloadButton.src = chrome.runtime.getURL("assets/icon-32.png");
      downloadButton.addEventListener("click", () => {
        download_port.postMessage({ bookId: bookId, token: token });
      });
      book.appendChild(downloadButton);
    }
  }
}