// decryptor.cpp
// (C) Martin Alebachew, 2023

#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <curl/curl.h>
#include <PDF/PDFNet.h>
#include <PDF/PDFDoc.h>
#include <PDF/PDFNetInternalTools.h>
#include <boost/filesystem.hpp>

#define PDFTRON_KEY "YOUR_TRIAL_KEY_HERE"

namespace fs = boost::filesystem;
using json = nlohmann::json;
using namespace pdftron;

typedef unsigned char byte;
struct DataBuffer {
  size_t written;
  size_t capacity;
  byte* buffer;

  DataBuffer() {
    capacity = 1024 * 1024 * 200; // Allocate 200MB
    buffer = (byte*)malloc(capacity); // TODO: Check for nullptr
    written = 0;
  }

  void Write(byte *newData, size_t size) {
    if (written + size > capacity) Expand();
    memcpy(buffer + written, newData, size);
    written += size;
  }

  byte* Expand() {
    capacity *= 1.5; // Aggressive expansion
    buffer = (byte*)realloc(buffer, capacity);
    return buffer;
  }

  byte* Shrink() {
    capacity = written;
    buffer = (byte*)realloc(buffer, capacity);
    return buffer;
  }

  ~DataBuffer() {
    free(buffer);
  }
};

size_t writeData(void *ptr, size_t size, size_t nmemb, FILE *stream) {
  DataBuffer *buffer = (DataBuffer*)stream;
  buffer->Write((byte*)ptr, size * nmemb);
  return size * nmemb;
}

bool downloadFile(const char *url, const DataBuffer *buffer) {
  CURL *curl = curl_easy_init();
  if (!curl) return false;

  curl_easy_setopt(curl, CURLOPT_URL, url);
  curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeData);
  curl_easy_setopt(curl, CURLOPT_WRITEDATA, buffer);

  CURLcode res = curl_easy_perform(curl);
  curl_easy_cleanup(curl);

  return !res;
}

json fetchRequest() {
  // Fetch request, according to the native messaging protocol
  uint32_t inputSize;
  std::cin.read((char*)&inputSize, sizeof(inputSize));
  char *inputString = new char[inputSize];
  std::cin.read(inputString, inputSize);
  json request = json::parse(inputString);

  // Get request fields
  std::string downloadUrl = request["downloadUrl"];
  std::string password = request["password"];
  std::string filename = request["filename"];

  return request;
}

void sendResponse(bool success, std::string field, std::string value) {
  // TODO: implement sending error message / downloaded filename
  // Set response fields
  json response;
  response["success"] = success;
  response[field] = value;

  // Send response, according to the native messaging protocol
  std::string responseString = response.dump();
  uint32_t responseSize(responseString.size());
  
  for (int i = 0; i < sizeof(uint32_t); i++) {
    std::cout << ((char*)&responseSize)[i];
  }

  std::cout << responseString.c_str() << std::flush;
}

void sendSuccess(std::string filename) {
  sendResponse(true, "filename", filename);
}

void sendFailure(std::string error) {
  sendResponse(false, "error", error);
}

int main(int argc, char **argv) {
  // Get request fields
  json request = fetchRequest();
  std::string downloadUrl = request["downloadUrl"];
  std::string password = request["password"];
  std::string filename = request["filename"];

  // Obtain target paths
  fs::path currentPath(fs::current_path()); // TODO: Replace with user's downloads path
  fs::path outputPath = currentPath / (filename + ".pdf");

  // Download PDF
  DataBuffer buffer;
  bool downloaded = downloadFile(downloadUrl.c_str(), &buffer);
  if (!downloaded) {
    sendFailure("Failed to download PDF!");
    return 1;
  }

  // Decrypt PDF
  // TODO: Implement exception handling

  // Disable PDFNet logging by redirecting stdout
  std::streambuf *old = std::cout.rdbuf(nullptr);

  PDFNet::Initialize(PDFTRON_KEY);
  PDF::PDFDoc document(buffer.Shrink(), buffer.written);
  bool decrypted = document.InitStdSecurityHandler(password);
  if (!decrypted) {
    sendFailure("Failed to decrypt PDF!");
    return 1;
  }

  document.RemoveSecurity();
  document.Save(outputPath.string(), SDF::SDFDoc::e_linearized);
  PDFNet::Terminate();

  // Enable stdout logging for native messaging
  std::cout.rdbuf(old);

  sendSuccess(outputPath.string());
  return 0;  
}