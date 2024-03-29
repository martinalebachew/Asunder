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

## Build & Install
### Prerequisites
- All operating systems - OpenSSL, Node.js, CMake and vcpkg.
- Windows - Visual Studio 2019 or higher.
- macOS - XCode Developer Tools.
- Linux - make, gcc.

### vcpkg
- Make sure vcpkg is in path.
- Install curl, nlohmann-json and boost-filesystem.
- If you are using an older release (before September 2023) of vcpkg for Windows, specify the target triplet manually when installing the packages listed above.

### Installation Scripts
1. Get your key from [Apryse Developer Portal](https://dev.apryse.com/). Paste it into decryptor/src/pdf.hpp.
2. Run scripts/install_asunder.py.
3. Manually load the extension into Chrome, instructions will appear after compilation is done.

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

## Native Messaging
The communication between the extension and the decryptor is possible thanks to 
Chrome's native messaging protocol. To allow this communication, you'll have to 
register a native messaging host, using a json file (see example file above). 
On Windows, we'll also need to create a matching registry key for our 
configuration file. 
[Read more in the official documentation.](https://developer.chrome.com/docs/apps/nativeMessaging/)
