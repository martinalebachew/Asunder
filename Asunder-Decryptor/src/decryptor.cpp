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
  bool logToStdout = false;

  void append(std::string text) {
    if (logToStdout) std::cout << text << std::endl;
    else {
      if (!firstLine) logged_text += "\n";
      else firstLine = false;

      logged_text += text;
    }
  }

  void flush() {
    std::ofstream file("asdlog.txt");
    file.write(logged_text.c_str(), logged_text.size());
  }

  ~Log() {
    flush();
  }
};

int main(int argc, char **argv) {
  Log log;
  if (argc > 1) log.logToStdout = true;
}