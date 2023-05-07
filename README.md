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
> caused by using it.

## Development Map
### Asunder-Extension
- [x] Download buttons on bookshelf
- [x] Download button in book reader
- [x] Download and decryption data fetching
- [ ] Communication with Asunder-decryptor

### Asunder-Decryptor
- [ ] Communication with the extension
- [ ] PDF downloading using curl
- [ ] PDF decryption using Apryse binaries
- [ ] Modification of Apryse binaries

## Source of binaries
The source code for the binaries is proprietary and available only to Apryse.
Yet, the Apryse SDK for multiple languages contains a compiled dynamic library
binaries and SWIG wrappers. We use those binaries in Asunder-decryptor.
Future versions might use slightly modified versions of those binaries, that
does not include the Apryse watermark on downloaded PDFs and does not
require a trial key.
