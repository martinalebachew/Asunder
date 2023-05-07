// decryptor.cpp
// (C) Martin Alebachew, 2023

#include <iostream>
#include <fstream>
#include <boost/filesystem.hpp>
class Log {
private:
  bool firstLine = true;
  std:: string logged_text;

public:
  bool logToStdout = true;

  void append(std::string text) {
    if (logToStdout) std::cout << text << std::endl;
    else {
      if (!firstLine) logged_text += "\n";
      else firstLine = false;

      logged_text += text;
    }
  }

  void flush() {
    if (logToStdout) return;
    std::ofstream file("asdlog.txt");
    file.write(logged_text.c_str(), logged_text.size());
  }

  ~Log() {
    flush();
  }
};

int main(int argc, char **argv) {
  Log log;
  if (argc > 1) log.logToStdout = false;

  uint32_t inputSize;
  std::cin.read((char*)&inputSize, sizeof(inputSize));
  char *inputString = new char[inputSize];
  std::cin.read(inputString, inputSize);
  std::string response = R"({"success": true)";
  std::cout << (uint32_t)response.size();
  std::cout << response.c_str() << std::flush;
}