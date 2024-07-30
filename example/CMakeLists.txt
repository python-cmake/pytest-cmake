cmake_minimum_required(VERSION 3.20)

project(Example)

if (NOT "${CMAKE_CXX_STANDARD}")
    set(CMAKE_CXX_STANDARD 17 CACHE STRING "Default C++ standard")
endif()

if (WIN32)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)
endif()

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(Boost 1.70.0 REQUIRED)

if (NOT TARGET Boost::python)
    set(_py_version ${Python_VERSION_MAJOR}${Python_VERSION_MINOR})
    add_library(Boost::python ALIAS "Boost::python${_py_version}")
endif()

find_package(Pytest 4.6.11 REQUIRED)

enable_testing()

add_subdirectory(src)
add_subdirectory(test)
