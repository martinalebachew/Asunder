// decryptor.cpp
// (C) Martin Alebachew, 2023

#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <boost/filesystem.hpp>

using json = nlohmann::json;

int main(int argc, char **argv) {
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

  // Set response fields
  json response;
  response["success"] = true;

  // Send response, according to the native messaging protocol
  std::string responseString = response.dump(0);
  uint32_t responseSize(responseString.size());
  
  for (int i = 0; i < sizeof(uint32_t); i++) {
    std::cout << ((char*)&responseSize)[i];
  }

  std::cout << responseString.c_str() << std::flush;
}