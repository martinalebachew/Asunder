// download.cpp
// (C) Martin Alebachew, 2023

#include "download.hpp"

size_t WriteData(void *ptr, size_t size, size_t nmemb, FILE *stream) {
  DataBuffer *buffer = (DataBuffer*)stream;
  buffer->Write((byte*)ptr, size * nmemb);
  return size * nmemb;
}

bool DownloadFile(const char *url, const DataBuffer *buffer) {
  CURL *curl = curl_easy_init();
  if (!curl) return false;

  curl_easy_setopt(curl, CURLOPT_URL, url);
  curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteData);
  curl_easy_setopt(curl, CURLOPT_WRITEDATA, buffer);

  CURLcode res = curl_easy_perform(curl);
  curl_easy_cleanup(curl);

  return !res;
}
