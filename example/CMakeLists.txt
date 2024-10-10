cmake_minimum_required(VERSION 3.20)

project(Example)

if (NOT "${CMAKE_CXX_STANDARD}")
    set(CMAKE_CXX_STANDARD 17 CACHE STRING "Default C++ standard")
endif()

if (WIN32)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)
endif()

find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)
find_package(nanobind CONFIG REQUIRED)

find_package(Pytest 4.6.11 REQUIRED)

enable_testing()

add_subdirectory(src)
add_subdirectory(test)
