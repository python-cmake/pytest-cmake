.. _introduction:

************
Introduction
************

This project provides convenient ways to use :term:`Pytest` within a
:term:`CMake` project. The package can be discovered from a specific range of
versions on Linux, macOS or Windows using the `find_package
<https://cmake.org/cmake/help/latest/command/find_package.html>`_ function:

.. code-block:: cmake

    find_package(Pytest 8.2.1 REQUIRED)

A :func:`pytest_discover_tests` function is provided to simplify automatic
testing for C++ projects with Python bindings. It can create :term:`CTest` tests
for each Python test collected within a correct environment:

.. code-block:: cmake

    pytest_discover_tests(
        PythonTest
        LIBRARY_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        PYTHON_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        TRIM_FROM_NAME "^test_"
        DEPENDS MyLibrary
    )

Running the tests will display the status for each test collected as follows:

.. code-block:: console

        Start 1: PythonTest.greet_world
    1/4 Test #1: PythonTest.greet_world ...........   Passed    0.47 sec
        Start 2: PythonTest.greet_john
    2/4 Test #2: PythonTest.greet_john ............   Passed    0.47 sec
        Start 3: PythonTest.greet_julia
    3/4 Test #3: PythonTest.greet_julia ...........   Passed    0.47 sec
        Start 4: PythonTest.greet_michael
    4/4 Test #4: PythonTest.greet_michael .........   Passed    0.54 sec

.. seealso:: :ref:`tutorial`
