cmake_minimum_required(VERSION 3.7)
project(AES-TBOX)

set(CMAKE_CXX_STANDARD 14)

set(CMAKE_CXX_FLAGS "-static")
set(SOURCE_FILES victim.cpp Types.h AES-Encryption.cpp AES-Encryption.h AES-KeyExp.cpp AES-KeyExp.h)
add_executable(AES-TBOX ${SOURCE_FILES})
