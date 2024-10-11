.. _tutorial:

********
Tutorial
********

Once :ref:`integrated into your project <integration>`, the ``Pytest::Pytest``
target and the :func:`pytest_discover_tests` function are available for using.

.. _tutorial/target:

Using the target
================

Let's consider a project that wraps C++ logic with Python bindings. We need to
add a :file:`CMakeLists.txt` configuration file to include Python tests within
the same directory. The :term:`Pytest` command can easily be implemented using
the :term:`add_test` function:

.. code-block:: cmake

    add_test(
        NAME PythonTest
        COMMAND Pytest::Pytest ${CMAKE_CURRENT_SOURCE_DIR}
    )

For the tests to run, the :envvar:`PYTHONPATH` environment variable must be
updated to locate the built package library. We can use a generator expression
to resolve the path of the dependent target directory dynamically:

.. code-block:: cmake

    set_tests_properties(
        TEST PythonTest
        PROPERTY ENVIRONMENT
            PYTHONPATH=$<TARGET_FILE_DIR:MyLibrary>:$ENV{PYTHONPATH}
    )

The shared library might also be required during runtime execution, so its
location should be provided:

.. code-block:: cmake

    set_tests_properties(
        TEST PythonTest
        APPEND PROPERTY ENVIRONMENT
            LD_LIBRARY_PATH=$<TARGET_FILE_DIR:MyLibrary>:$ENV{LD_LIBRARY_PATH}
    )

.. warning::

    The environment variable used to locate shared libraries depends on the
    platform. :envvar:`LD_LIBRARY_PATH` is used on Linux,
    :envvar:`DYLD_LIBRARY_PATH` on macOS, and :envvar:`PATH` on Windows.

After building the project, the tests can then be executed using :term:`CTest`.
If all tests are successful, the output will look as follows:

.. code-block:: console

        Start 1: PythonTest
    1/1 Test #1: PythonTest .......................   Passed    0.55 sec

However, if only one test is unsuccessful, the entire test suite will be marked
as failed.

.. code-block:: console

        Start 1: PythonTest
    1/1 Test #1: PythonTest .......................***Failed    0.47 sec

.. _tutorial/function:

Using the function
==================

A :func:`pytest_discover_tests` function is provided to create :term:`CMake`
tests for each Python test collected. Therefore, the configuration added in the
previous section could be replaced by the following:

.. code-block:: cmake

    pytest_discover_tests(
        PythonTest
        LIBRARY_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        PYTHON_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        DEPENDS MyLibrary
    )

This will create a new **PythonTest** target, dependent on the **MyLibrary**
target.

The expected environment can be defined simply with the ``LIBRARY_PATH_PREPEND``
and ``PYTHON_PATH_PREPEND`` options, which both accept multiple values. The
environment variable used to locate shared libraries will be automatically
chosen according to the platform.

A list of dependent targets can be defined with the ``DEPENDS`` option, which
accepts multiple values.

After building the project, running :term:`CTest` will display the tests as
follows:

.. code-block:: console

        Start 1: PythonTest.test_greet_world
    1/4 Test #1: PythonTest.test_greet_world ...........   Passed    0.47 sec
        Start 2: PythonTest.test_greet_john
    2/4 Test #2: PythonTest.test_greet_john ............   Passed    0.47 sec
        Start 3: PythonTest.test_greet_julia
    3/4 Test #3: PythonTest.test_greet_julia ...........   Passed    0.47 sec
        Start 4: PythonTest.test_greet_michael
    4/4 Test #4: PythonTest.test_greet_michael .........   Passed    0.54 sec

A fully identified test collected by :term:`Pytest` might look like this:

.. code-block:: console

    tests/test_module.py::TestMyClass::test_example

By default, only the class and function name of each :term:`Pytest` test collected
are used to create the :term:`CMake` tests. You can use the ``INCLUDE_FILE_PATH``
option to include the file path within the name:

.. code-block:: cmake
   :emphasize-lines: 7

    pytest_discover_tests(
        PythonTest
        LIBRARY_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        PYTHON_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        INCLUDE_FILE_PATH
        DEPENDS MyLibrary
    )

Pytest usually requires the test class and function to start with a
`specific prefix
<https://docs.pytest.org/en/latest/explanation/goodpractices.html>`_,
which can be trimmed using the ``TRIM_FROM_NAME`` or ``TRIM_FROM_FULL_NAME``
options. The value can use a :term:`regular expression` to match the part of
the test name that should be trimmed.

The ``TRIM_FROM_FULL_NAME`` option can be used to trim parts of the entire name,
while the ``TRIM_FROM_NAME`` option will be applied to the class, method and
function name of each :term:`Pytest` test collected for convenience.

.. code-block:: cmake
   :emphasize-lines: 7

    pytest_discover_tests(
        PythonTest
        LIBRARY_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        PYTHON_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        TRIM_FROM_NAME "^(Test|test_)"
        INCLUDE_FILE_PATH
        DEPENDS MyLibrary
    )

After rebuilding the project, running :term:`CTest` will display the tests as
follows:

.. code-block:: console

        Start 1: PythonTest.greet_world
    1/4 Test #1: PythonTest.greet_world ...............   Passed    0.47 sec
        Start 2: PythonTest.greet_john
    2/4 Test #2: PythonTest.greet_john ................   Passed    0.47 sec
        Start 3: PythonTest.greet_julia
    3/4 Test #3: PythonTest.greet_julia ...............   Passed    0.47 sec
        Start 4: PythonTest.subfolder.greet_michael
    4/4 Test #4: PythonTest.subfolder.greet_michael ...   Passed    0.54 sec

It is also possible to regroup all tests under one :term:`CTest` test, as
was the case when :ref:`using the target <tutorial/target>`. This can be
useful during development to ensure that the tests run faster, especially
if you use :term:`fixtures <fixture>` with a broader scope.

This can be done by setting the ``BUNDLE_TESTS`` option to True:

.. code-block:: cmake
   :emphasize-lines: 8

    pytest_discover_tests(
        PythonTest
        LIBRARY_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        PYTHON_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        DEPENDS MyLibrary
        BUNDLE_TESTS True
    )

After rebuilding the project once again, running :term:`CTest` will display the
tests as follows:

.. code-block:: console

        Start 1: PythonTest
    1/1 Test #1: PythonTest .......................   Passed    0.51 sec

.. note::

    The :envvar:`BUNDLE_PYTHON_TESTS` environment variable can also set this
    option dynamically.

