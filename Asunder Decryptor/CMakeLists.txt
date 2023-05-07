cmake_minimum_required(VERSION 3.26)
project(decryptor)
set(CMAKE_CXX_STANDARD 17)

set(SOURCE_FILES src/decryptor.cpp)
add_executable(decryptor ${SOURCE_FILES})