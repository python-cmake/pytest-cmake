.. _api_reference:

*************
API Reference
*************

.. highlight:: cmake

.. function:: pytest_discover_tests(NAME ARGV)

    Automatically create :term:`CTest` tests for Python tests collected
    with :term:`Pytest` within a controlled environment::

        pytest_discover_tests(NAME
            [WORKING_DIRECTORY dir]
            [TRIM_FROM_NAME pattern]
            [TRIM_FROM_FULL_NAME pattern]
            [LIBRARY_PATH_PREPEND path1 path2...]
            [PYTHON_PATH_PREPEND path1 path2...]
            [ENVIRONMENT env1 env2...]
            [PROPERTIES prop1 prop2...]
            [DEPENDS target1 target2...]
            [INCLUDE_FILE_PATH]
            [STRIP_PARAM_BRACKETS]
            [BUNDLE_TESTS]
        )

    The options are:

    * ``NAME``

        Indicate the name of the target that will be created. It will also be
        used as a prefix for each test created, or as an identifier the bundled
        test.

    * ``WORKING_DIRECTORY``

        Specify the directory in which to run the :term:`Pytest` command. If
        this option is not provided, the current source directory is used.

    * ``INCLUDE_FILE_PATH``

        Include the file path of each collected :term:`Pytest` test into its generated
        test name. This helps distinguish tests with the same class or function names
        by including their source file for clearer identification::

            pytest_discover_tests(
                ...
                INCLUDE_FILE_PATH
            )

    * ``TRIM_FROM_NAME``

        Specify a :term:`regular expression` to trim part of each
        class, method and function name discovered before creating the test.
        This option can be used to trim the convention prefix required by
        :term:`Pytest` for discovery::

            pytest_discover_tests(
                ...
                TRIM_FROM_NAME "^(Test|test_)"
            )

    * ``TRIM_FROM_FULL_NAME``

        Specify a :term:`regular expression` to trim parts of the full test name
        generated::

            pytest_discover_tests(
                ...
                TRIM_FROM_FULL_NAME "(Test|test_)"
            )

    * ``STRIP_PARAM_BRACKETS``

        Remove square brackets added to the test identifier when using
        :term:`parametrized tests <parametrizing tests>`::

            pytest_discover_tests(
                ...
                STRIP_PARAM_BRACKETS
            )

        Tests identifiers will be reformatted as follows:

        - `test.foo[bar]` becomes `test.foo.bar`
        - `test.foo[1-3]` becomes `test.foo.1-3`
        - `test.foo[bar[nested]]` becomes `test.foo.bar[nested]`

    * ``LIBRARY_PATH_PREPEND``

        List of library paths to prepend to the corresponding environment
        variable (:envvar:`LD_LIBRARY_PATH` on Linux,
        :envvar:`DYLD_LIBRARY_PATH` on macOS, and :envvar:`PATH` on Windows)
        when running the tests. Each path can be defined literally or as a CMake
        expression generator for convenience::

            pytest_discover_tests(
                ...
                LIBRARY_PATH_PREPEND
                    $<TARGET_FILE_DIR:lib1>
                    $<TARGET_FILE_DIR:lib2>
                    /path/to/libs/
            )

    * ``PYTHON_PATH_PREPEND``

        List of Python paths to prepend to the :envvar:`PYTHONPATH` environment
        variable when running the tests. Each path can be defined literally or
        as a CMake expression generator for convenience::

            pytest_discover_tests(
                ...
                PYTHON_PATH_PREPEND
                    $<TARGET_FILE_DIR:lib1>
                    $<TARGET_FILE_DIR:lib2>
                    /path/to/python/
            )

    * ``ENVIRONMENT``

        List of custom environment variables with associated values to set when
        running the tests::

            pytest_discover_tests(
                ...
                ENVIRONMENT
                    "ENV_VAR1=VALUE1"
                    "ENV_VAR2=VALUE2"
                    "ENV_VAR3=VALUE3"
            )

    * ``PROPERTIES``

        List of custom `test properties
        <https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html#test-properties>`_
        to apply for all generated tests::

            pytest_discover_tests(
                ...
                PROPERTIES
                    LABELS "python;unit"
                    TIMEOUT 120
            )

    * ``DEPENDS``

        List of dependent targets that need to be executed before running
        the tests::

            pytest_discover_tests(
                ...
                DEPENDS lib1 lib2
            )

    * ``BUNDLE_TESTS``

        Indicate whether Python tests should be bundled under a single
        :term:`CTest` test. This option can also be set dynamically by using
        the :envvar:`BUNDLE_PYTHON_TESTS` environment variable.

        Bundled tests generally run faster because :term:`Pytest` can use
        caching and :term:`fixtures <fixture>` with a broader scope.

    .. note::

       This function works similarly to the `gtest_discover_tests
       <https://cmake.org/cmake/help/latest/module/GoogleTest.html#command:gtest_discover_tests>`_
       function, which creates :term:`CTest` tests for each :term:`GTest` tests
       discovered within a single C++ executable test file.

