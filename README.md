# Pytest CMake

[![Test](https://github.com/buddly27/pytest-cmake/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/buddly27/pytest-cmake/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CMake](https://img.shields.io/badge/CMake-3.20...3.25-blue.svg)](https://cmake.org)

Discover and run Python tests for [Pytest](https://docs.pytest.org/) with 
[CMake](https://cmake.org/). This module simplify Python automatic testing for 
C++ project with Python Bindings.

It works on Linux, macOS and Windows.

## Usage

First, ensure that Pytest is installed on your platform by adding the following
dependency in your project:

```cmake
find_package(Pytest REQUIRED)
```

It is recommended to specify a minimum version for safety:

```cmake
find_package(Pytest 4.6.11 REQUIRED)
```

Then add a CMake configuration file within your Python test directory with
the following function:

```cmake
pytest_discover_tests(
    PythonTest
    LIBRARY_PATH_PREPEND
        $<TARGET_FILE_DIR:example>
    PYTHON_PATH_PREPEND
        $<TARGET_FILE_DIR:example>
    TRIM_FROM_NAME "^test_"
    DEPENDS example
)
```

The first argument represent the name of the CMake target which will be created.
It will also be used as a prefix for all tests displayed within 
[CTest](https://cmake.org/cmake/help/latest/manual/ctest.1.html).

Expected environment can be defined with the ``LIBRARY_PATH_PREPEND`` and
``PYTHON_PATH_PREPEND`` arguments, which both accept multiple values. In our
example, we use an expression generator to link to the target used for building
the Python library.

Pytest usually requires tests to start with a
[specific prefix](https://docs.pytest.org/en/latest/explanation/goodpractices.html), 
which can be trimmed using the ``TRIM_FROM_NAME`` argument.

Targets dependency can be defined with the ``DEPENDS`` argument, which accept 
multiple values.

By default, running CTest for the project will display the tests as follows:

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

By setting the ``BUNDLE_TESTS`` argument to True, all tests will be grouped into
one CMake test:

```console
    Start 1: PythonTest
1/1 Test #1: PythonTest .......................   Passed    0.51 sec
```

This argument can also be set by the ``BUNDLE_PYTHON_TESTS`` environment
variable. Bundling the tests will limit the visibility of all discovered test
with CTest, but it will ensure that the tests can run faster in case you are 
using [fixture](https://docs.pytest.org/en/latest/explanation/fixtures.html) 
with a wider scope.

Finally, ensure that ``FindPytest.cmake`` and ``PytestAddTests.cmake`` are
available via [CMAKE_MODULE_PATH](https://cmake.org/cmake/help/latest/variable/CMAKE_MODULE_PATH.html)
and do not forget to [install Pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) 
with the required version.

An example project is available for more details.