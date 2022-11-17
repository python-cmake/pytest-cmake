cmake_minimum_required(VERSION 3.20)

project(Example)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
set(_py_version ${Python_VERSION_MAJOR}${Python_VERSION_MINOR})
mark_as_advanced(_py_version)

find_package(Boost 1.70.0 COMPONENTS "python${_py_version}" REQUIRED)

if (NOT TARGET Boost::python)
    add_library(Boost::python ALIAS "Boost::python${_py_version}")
endif()

find_package(Pytest 4.6.11 REQUIRED)

enable_testing()

add_subdirectory(src)
add_subdirectory(test)
