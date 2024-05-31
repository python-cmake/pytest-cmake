.. _tutorial:

********
Tutorial
********

Once :ref:`integrated in your project <integration>`, the ``Pytest::Pytest``
target and the :func:`pytest_discover_tests` function are available for using.

.. _tutorial/target:

Using the target
================

Let's consider a project which wraps C++ logic with Python bindings. We need to
add a :file:`CMakeLists.txt` configuration file to add Python tests within the
same directory. The :term:`Pytest` command can be easily implemented using the
:term:`add_test` function:

.. code-block:: cmake

    add_test(
        NAME PythonTest
        COMMAND Pytest::Pytest ${CMAKE_CURRENT_SOURCE_DIR}
    )

For the tests to run, the :envvar:`PYTHONPATH` environment variable must be
updated to locate the built package library. We can use an expression generator
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

After building the project, the command can then be executed by :term:`CTest`.
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

A :func:`pytest_discover_tests` function is provided to create :term:`CTest`
tests for each Python test collected. Therefore, the configuration added in the
previous section could be replaced by the following:

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

This will create a new **PythonTest** target, dependent on the **MyLibrary**
target.

The expected environment can be defined simply with the ``LIBRARY_PATH_PREPEND``
and ``PYTHON_PATH_PREPEND`` arguments, which both accept multiple values. The
environment variable used to locate shared libraries will be automatically
chosen according to the platform.

Pytest usually requires tests to start with a
`specific prefix
<https://docs.pytest.org/en/latest/explanation/goodpractices.html>`_,
which can be trimmed using the ``TRIM_FROM_NAME`` argument. The value can use a
`regular expression <https://en.wikipedia.org/wiki/Regular_expression>`_ to
match the part of the test name that should be trimmed.

A list of dependent targets can be defined with the ``DEPENDS`` argument, which
accepts multiple values.

After building the project, running :term:`CTest` will display the tests as
follows:

.. code-block:: console

        Start 1: PythonTest.greet_world
    1/4 Test #1: PythonTest.greet_world ...........   Passed    0.47 sec
        Start 2: PythonTest.greet_john
    2/4 Test #2: PythonTest.greet_john ............   Passed    0.47 sec
        Start 3: PythonTest.greet_julia
    3/4 Test #3: PythonTest.greet_julia ...........   Passed    0.47 sec
        Start 4: PythonTest.greet_michael
    4/4 Test #4: PythonTest.greet_michael .........   Passed    0.54 sec

It is also possible to regroup all tests under one :term:`CTest` test, as
was the case when :ref:`using the target <tutorial/target>`. This can be
useful during development to ensure that the tests run faster, especially
if you use :term:`fixtures <fixture>` with a broader scope.

This can be done by setting the ``BUNDLE_TESTS`` argument to True:

.. code-block:: cmake
   :emphasize-lines: 9

    pytest_discover_tests(
        PythonTest
        LIBRARY_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        PYTHON_PATH_PREPEND
            $<TARGET_FILE_DIR:MyLibrary>
        TRIM_FROM_NAME "^test_"
        DEPENDS MyLibrary
        BUNDLE_TESTS True
    )

After re-building the project, running :term:`CTest` will display the tests as
follows:

.. code-block:: console

        Start 1: PythonTest
    1/1 Test #1: PythonTest .......................   Passed    0.51 sec

.. note::

    The :envvar:`BUNDLE_PYTHON_TESTS` environment variable can also set this
    argument dynamically.

