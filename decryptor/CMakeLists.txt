cmake_minimum_required(VERSION 3.26)
project(decryptor)
set(CMAKE_CXX_STANDARD 17)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY         ${CMAKE_SOURCE_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG   ${CMAKE_SOURCE_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_SOURCE_DIR}/bin)

include_directories(${Boost_INCLUDE_DIRS})
find_package(Boost REQUIRED COMPONENTS filesystem)
set(used_libs )

find_package(nlohmann_json REQUIRED)
find_package(CURL REQUIRED)

include_directories(${CMAKE_SOURCE_DIR}/dep/PDFNetC/Headers)
link_directories(${CMAKE_SOURCE_DIR}/dep/PDFNetC/Lib)

file(GLOB SOURCE_FILES src/*.cpp)
add_executable(decryptor ${SOURCE_FILES})

target_link_libraries(decryptor ${Boost_FILESYSTEM_LIBRARY} nlohmann_json::nlohmann_json CURL::libcurl PDFNetC)
target_precompile_headers(decryptor PRIVATE 
  <iostream> <cstring> <chrono> <fstream> 
  <nlohmann/json.hpp> <PDF/PDFNet.h> <PDF/PDFDoc.h> <boost/filesystem.hpp> <curl/curl.h>
  <fcntl.h>
)
