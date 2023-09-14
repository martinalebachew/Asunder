cmake_minimum_required(VERSION 3.26)
project(decryptor)
set(CMAKE_CXX_STANDARD 17)

include_directories(${Boost_INCLUDE_DIRS})
find_package(Boost REQUIRED COMPONENTS filesystem)
set(used_libs ${Boost_FILESYSTEM_LIBRARY})

find_package(nlohmann_json REQUIRED)
find_package(CURL REQUIRED)

include_directories(${CMAKE_SOURCE_DIR}/dep/PDFNetC/Headers)
link_directories(${CMAKE_SOURCE_DIR}/dep/PDFNetC/Lib)

file(GLOB SOURCE_FILES src/*.cpp)
add_executable(decryptor ${SOURCE_FILES})

target_link_libraries(decryptor ${used_libs})
target_link_libraries(decryptor nlohmann_json::nlohmann_json)
target_link_libraries(decryptor CURL::libcurl)
target_link_libraries(decryptor PDFNetC)