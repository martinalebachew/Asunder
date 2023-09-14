// browser_io.cpp
// (C) Martin Alebachew, 2023

#include "browser_io.hpp"

namespace BrowserIO {
  json FetchRequest() {
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

  void SendResponse(bool success, std::string field, std::string value) {
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

  void SendSuccess(std::string filename) {
    SendResponse(true, "filename", filename);
  }

  void SendFailure(std::string error) {
    SendResponse(false, "error", error);
  }
}
