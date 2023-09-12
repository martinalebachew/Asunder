// download.hpp
// (C) Martin Alebachew, 2023

#pragma once
#include "data_buffer.hpp"
#include <fstream>
#include <curl/curl.h>
#include <boost/filesystem.hpp>

namespace fs = boost::filesystem;

size_t WriteData(void *ptr, size_t size, size_t nmemb, FILE *stream);
bool DownloadFile(const char *url, const DataBuffer *buffer);
