// browser_io.hpp
// (C) Martin Alebachew, 2023

#pragma once
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

namespace BrowserIO {
  json FetchRequest();
  void SendResponse(bool success, std::string field, std::string value);
  void SendSuccess(std::string filename);
  void SendFailure(std::string error);
};
