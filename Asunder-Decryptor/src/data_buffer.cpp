// data_buffer.cpp
// (C) Martin Alebachew, 2023

#include "data_buffer.hpp"

DataBuffer::DataBuffer() {
  capacity = 1024 * 1024 * 200; // Allocate 200MB
  buffer = (byte*)malloc(capacity); // TODO: Check for nullptr
  written = 0;
}

DataBuffer::~DataBuffer() {
  free(buffer);
}

void DataBuffer::Write(byte *newData, size_t size) {
  if (written + size > capacity) Expand();
  memcpy(buffer + written, newData, size);
  written += size;
}

byte* DataBuffer::Expand() {
  capacity *= 1.5; // Aggressive expansion
  buffer = (byte*)realloc(buffer, capacity);
  return buffer;
}

byte* DataBuffer::Shrink() {
  capacity = written;
  buffer = (byte*)realloc(buffer, capacity);
  return buffer;
}

size_t DataBuffer::GetWritten() {
  return written;
}
