# Asunder

Asunder is a Chrome extension for downloading Classoos digital textbooks as PDFs.
This repository contains the extension, which retrieves all other relevant information for
download and decryption. Then, the extension communicates with another application,
**Asunder-decryptor**, which downloads the PDF file and calls the Apryse (PDFTron) dynamic
library binaries (or slightly modified versions). Those binaries remove the PDF
encryption and convert it to comply with most readers.
