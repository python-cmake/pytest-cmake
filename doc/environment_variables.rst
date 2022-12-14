.. _environment_variables:

*********************
Environment variables
*********************

Environment variables directly defined or referenced by this package.

.. envvar:: BUNDLE_PYTHON_TESTS

    Environment variable used to dynamically set a value for the
    ``BUNDLE_TESTS`` argument of the :func:`pytest_discover_tests` function.

    .. seealso:: :ref:`Using 'pytest_discover_tests' <getting_started/function>`

.. envvar:: LD_LIBRARY_PATH

    Environment variable used on Linux/UNIX System to locate shared libraries.

.. envvar:: DYLD_LIBRARY_PATH

    Environment variable used on macOS System to locate shared libraries.

.. envvar:: PATH

    Environment variable used to specifies the directories to be searched to
    find a command. On Windows system, this environment variable is also used
    to locate shared libraries.
