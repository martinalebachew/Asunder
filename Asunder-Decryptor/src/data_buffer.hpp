// data_buffer.hpp
// (C) Martin Alebachew, 2023

#pragma once
#include <iostream>
#include <cstring>

typedef unsigned char byte;

class DataBuffer {
private:
  size_t written;
  size_t capacity;
  byte* buffer;

public:
  void Write(byte *newData, size_t size);
  byte* Expand();
  byte* Shrink();
  size_t GetWritten();

  DataBuffer();
  ~DataBuffer();
};
