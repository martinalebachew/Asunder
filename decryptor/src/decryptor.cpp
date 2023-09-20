// decryptor.cpp
// (C) Martin Alebachew, 2023

#include "browser_io.hpp"
#include "data_buffer.hpp"
#include "download.hpp"
#include "pdf.hpp"
#include <iostream>
#include <chrono>
#include <fcntl.h>

#ifdef _WIN32
#include <io.h>
#define NULL_DEVICE "nul"
#define O_WRONLY _O_WRONLY
#else
#include <unistd.h>
#define NULL_DEVICE "/dev/null"
#endif

int main(int argc, char **argv) {
  #ifdef _WIN32
  // Change I/O mode to prevent Windows from tampering with stdout
  _setmode(_fileno(stdout), _O_BINARY);
  #endif

  // Initialize log file
  using namespace std::chrono;
  nanoseconds ns = duration_cast<nanoseconds>(
      system_clock::now().time_since_epoch()
  );

  std::string log_name = std::to_string(ns.count());
  log_name += ".log";
  std::ofstream log(log_name);
  // TODO: Move to logs folder
  // TODO: Name regeneration on failure

  // Get request fields
  json request = BrowserIO::FetchRequest();
  log << "Got request: " << request.dump(2) << std::endl;

  std::string downloadUrl = request["downloadUrl"];
  std::string password = request["password"];
  std::string filename = request["filename"];

  // Obtain target paths
  fs::path currentPath(fs::current_path()); // TODO: Replace with user's downloads path
  fs::path outputPath = currentPath / filename;
  log << "Calculated output path: " << outputPath.string() << std::endl;

  // Download PDF
  DataBuffer buffer;
  bool downloaded = DownloadFile(downloadUrl.c_str(), &buffer);
  if (!downloaded) {
    log << "Failed to download PDF!" << std::endl;
    log.close();

    BrowserIO::SendFailure("Failed to download PDF!");
    return 1;
  }
  
  log << "Downloaded PDF of size: " << buffer.GetWritten()<<  "bytes." << std::endl;

  // Decrypt PDF
  // TODO: Implement exception handling

  // Disable PDFNet logging by redirecting stdout
  fflush(stdout);
  int stdout_backup_fd = dup(1);
  int null_fd = open(NULL_DEVICE, O_WRONLY);
  dup2(null_fd, 1);
  close(null_fd);

  log << "Initializing PDFTron with key: " << PDFTRON_KEY << std::endl;
  InitializePDFTron();

  PDF document(buffer.Shrink(), buffer.GetWritten());

  if (!document.Decrypt(password)) {
    log << "Failed to decrypt PDF!" << std::endl;
    log.close();

    BrowserIO::SendFailure("Failed to decrypt PDF!");
    return 1;
  }

  log << "Decrypted PDF." << std::endl;

  document.Save(outputPath.string());
  log << "Saved PDF into " << outputPath.string() << std::endl;

  TerminatePDFTron();
  
  // Enable stdout logging for native messaging
  fflush(stdout);
  dup2(stdout_backup_fd, 1);
  close(stdout_backup_fd);

  log << "Done." << std::endl;
  log.close();

  BrowserIO::SendSuccess(outputPath.string());
  return 0;
}
