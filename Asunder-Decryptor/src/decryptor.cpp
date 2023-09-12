// decryptor.cpp
// (C) Martin Alebachew, 2023

#include "browser_io.hpp"
#include "data_buffer.hpp"
#include "download.hpp"
#include "pdf.hpp"
#include <iostream>

int main(int argc, char **argv) {
  // Get request fields
  json request = BrowserIO::FetchRequest();
  std::string downloadUrl = request["downloadUrl"];
  std::string password = request["password"];
  std::string filename = request["filename"];

  // Obtain target paths
  fs::path currentPath(fs::current_path()); // TODO: Replace with user's downloads path
  fs::path outputPath = currentPath / (filename + ".pdf");

  // Download PDF
  DataBuffer buffer;
  bool downloaded = DownloadFile(downloadUrl.c_str(), &buffer);
  if (!downloaded) {
    BrowserIO::SendFailure("Failed to download PDF!");
    return 1;
  }

  // Decrypt PDF
  // TODO: Implement exception handling

  // Disable PDFNet logging by redirecting stdout
  std::streambuf *old = std::cout.rdbuf(nullptr);

  PDF document(buffer.Shrink(), buffer.GetWritten());
  if (!document.Decrypt(password)) {
    BrowserIO::SendFailure("Failed to decrypt PDF!");
    return 1;
  }

  document.Save(outputPath.string());
  
  // Enable stdout logging for native messaging
  std::cout.rdbuf(old);

  BrowserIO::SendSuccess(outputPath.string());
  return 0;  
}
