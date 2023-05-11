# Asunder

Asunder is a Chrome extension for downloading Classoos digital textbooks as PDFs.
This repository contains the extension, which retrieves all other relevant information for
download and decryption. Then, the extension communicates with another application,
**Asunder-Decryptor**, which downloads the PDF file and calls the Apryse (PDFTron) dynamic
library binaries (or slightly modified versions). Those binaries remove the PDF
encryption and convert it to comply with most readers.

> **Disclaimer**
> By using this extension, you understand the risk of banning or legal actions, and take full
> responsiblity for any violation of Classoos TOS (TL;DR). This project was made for educational
> purposes only, and the author of this project is not responsible for any potential consequences
> of using it.

## Development Map
### Asunder-Extension
- [x] Download buttons on bookshelf
- [ ] Download button in book reader
- [x] Download and decryption data fetching
- [x] Communication with Asunder-decryptor

### Asunder-Decryptor
- [x] Communication with the extension
- [x] PDF downloading using curl
- [x] PDF decryption and linearization
- [ ] Modifications of PDFNetC

## Modified PDFNetC
PDFNetC is the official Apryse C++ library used in Asunder for decryption.
Future versions might use slightly modified versions of those binaries, that
does not include the Apryse watermark on downloaded PDFs nor require a trial key.
