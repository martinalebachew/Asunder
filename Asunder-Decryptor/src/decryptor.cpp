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

size_t write_data(void *ptr, size_t size, size_t nmemb, FILE *stream) {
  size_t written = fwrite(ptr, size, nmemb, stream);
  return written;
}

bool downloadFile(const char *url, const char *filename) {
  CURL *curl = curl_easy_init();
  if (!curl) return false;

  FILE *file = fopen(filename, "wb");
  if (!file) return false;

  curl_easy_setopt(curl, CURLOPT_URL, url);
  curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
  curl_easy_setopt(curl, CURLOPT_WRITEDATA, file);

  CURLcode res = curl_easy_perform(curl);
  curl_easy_cleanup(curl);
  fclose(file);

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

void sendResponse(bool success) {
  // Set response fields
  json response;
  response["success"] = success;

  // Send response, according to the native messaging protocol
  std::string responseString = response.dump();
  uint32_t responseSize(responseString.size());
  
  for (int i = 0; i < sizeof(uint32_t); i++) {
    std::cout << ((char*)&responseSize)[i];
  }

  std::cout << responseString.c_str() << std::flush;
}

int main(int argc, char **argv) {
  // Get request fields
  json request = fetchRequest();
  std::string downloadUrl = request["downloadUrl"];
  std::string password = request["password"];
  std::string filename = request["filename"];

  // Obtain target paths
  fs::path currentPath(fs::current_path()); // TODO: Replace with user's downloads path
  fs::path tempPath = currentPath / (filename + ".tmp");
  fs::path outputPath = currentPath / (filename + ".pdf");

  // Download PDF
  bool downloaded = downloadFile(downloadUrl.c_str(), tempPath.c_str());
  if (!downloaded) {
    sendResponse(false);
    return 1;
  }

  // Decrypt PDF
  // TODO: Implement temp buffer
  // TODO: Implement exception handling

  // Disable PDFNet logging by redirecting stdout
  std::streambuf *old = std::cout.rdbuf(nullptr);

  PDFNet::Initialize(PDFTRON_KEY);
  PDF::PDFDoc document(tempPath.string());
  document.InitStdSecurityHandler(password);
  document.RemoveSecurity();
  document.Save(outputPath.string(), SDF::SDFDoc::e_linearized);
  PDFNet::Terminate();

  // Enable stdout logging for native messaging
  std::cout.rdbuf(old);

  sendResponse(true);
}