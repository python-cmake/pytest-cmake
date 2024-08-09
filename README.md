# Pytest CMake

[![PyPi version](https://img.shields.io/pypi/v/pytest-cmake.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.python.org/pypi/pytest-cmake)
[![CMake](https://img.shields.io/badge/CMake-3.20...3.30-blue.svg?logo=CMake&logoColor=blue)](https://cmake.org)
[![Test](https://github.com/python-cmake/pytest-cmake/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/python-cmake/pytest-cmake/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project provides convenient ways to use [Pytest](https://docs.pytest.org/)
within a [CMake](https://cmake.org/) project. The package can be discovered from a specific range of
versions on Linux, macOS or Windows using the
[find_package](https://cmake.org/cmake/help/latest/command/find_package.html)
function:

```cmake
find_package(Pytest 8.2.1 REQUIRED)
```

A ``pytest_discover_tests`` function is provided to simplify automatic
testing for C++ projects with Python bindings. It can create CTest tests
for each Python test collected within a controlled environment:

```cmake
pytest_discover_tests(
    PythonTest
    LIBRARY_PATH_PREPEND
        $<TARGET_FILE_DIR:MyLibrary>
    PYTHON_PATH_PREPEND
        $<TARGET_FILE_DIR:MyLibrary>
    TRIM_FROM_NAME "^test_"
    DEPENDS MyLibrary
)
```

Running the tests will display the status for each test collected as follows:

```console
    Start 1: PythonTest.greet_world
1/4 Test #1: PythonTest.greet_world ...........   Passed    0.47 sec
    Start 2: PythonTest.greet_john
2/4 Test #2: PythonTest.greet_john ............   Passed    0.47 sec
    Start 3: PythonTest.greet_julia
3/4 Test #3: PythonTest.greet_julia ...........   Passed    0.47 sec
    Start 4: PythonTest.greet_michael
4/4 Test #4: PythonTest.greet_michael .........   Passed    0.54 sec
```

## Documentation

Full documentation, including installation and setup guides, can be found at
https://python-cmake.github.io/pytest-cmake/
