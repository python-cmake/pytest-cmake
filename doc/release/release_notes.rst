.. _release/release_notes:

*************
Release Notes
*************

.. release:: Upcoming

    .. change:: fixed

        Corrected the CMake version upper bound from 3.30 to 3.31.

    .. change:: changed

        Added documentation for :ref:`installing/deployment`.

    .. change:: changed

        Added link to Github Project in documentation.

.. release:: 0.8.3
    :date: 2024-08-16

    .. change:: fixed

        Fixed the :func:`pytest_discover_tests` function by serializing
        the `ENVIRONMENT` entries before transferring them to the
        intermediate script.

.. release:: 0.8.2
    :date: 2024-08-09

    .. change:: new

        Added compatibility with CMake 3.30.

.. release:: 0.8.1
    :date: 2024-08-08

    .. change:: fixed

        Ensure that the 'PYTEST_EXECUTABLE' variable is correctly serialized
        when the tests are created to handle cases where the path might
        contain spaces or special characters.

.. release:: 0.8.0
    :date: 2024-08-01

    .. change:: changed

        Improved the :func:`pytest_discover_tests` function to use an
        intermediate CMake script during :term:`CTest` runs. This update
        enables partial builds that exclude the corresponding CMake target
        to be executed and tested.

.. release:: 0.7.0
    :date: 2024-05-31

    .. change:: fixed

        Updated CMake script to enable the trimming of class and method
        names on discovered tests.

    .. change:: changed

        Updated documentation.

.. release:: 0.6.0
    :date: 2024-05-11

    .. change:: changed

        Updated CMake script to ensure that environment variables are
        preserving the Windows-style path syntax when running the tests.

        .. seealso:: https://github.com/python-cmake/pytest-cmake/issues/22

    .. change:: changed

        Improve tests.

.. release:: 0.5.2
    :date: 2024-05-06

    .. change:: fixed

        Updated test collection logic to ensure that the 'rootdir' is a
        real path. Previously, running the tests from a symlinked directory
        could result in errors when discovering 'conftests' configurations.

        .. seealso:: https://github.com/pytest-dev/pytest/issues/12291

.. release:: 0.5.1
    :date: 2024-03-17

    .. change:: fixed

        Fixed CI Deployment script.

.. release:: 0.5.0
    :date: 2024-03-17

    .. change:: changed

        Updated CMake script now interrupts the build if the Python test
        collection fails.

.. release:: 0.4.1
    :date: 2024-03-17

    .. change:: fixed

        As of Hatching v1.22, dynamic dependencies during build time must
        be imported lazily. Therefore, the backend script has been updated
        to import 'pytest' only when the build hook is called.

        .. seealso::

            `BuildHookInterface.dependencies
            <https://hatch.pypa.io/dev/plugins/build-hook/reference/#hatchling.builders.hooks.plugin.interface.BuildHookInterface.dependencies>`_

.. release:: 0.4.0
    :date: 2024-03-03

    .. change:: fixed

        Fixed CMake script to ensure that library and Python path list
        environment variables are represented as strings before
        serializing the CTest commands.

    .. change:: changed

        Updated Github CI script to run all tests once a week.

    .. change:: new

        Added compatibility with Pytest v8 and CMake 3.29.

.. release:: 0.3.0
    :date: 2023-07-18

    .. change:: new

        Added ``ENVIRONMENT`` argument to the :func:`pytest_discover_tests`
        function to provide custom environment variables during the tests.

        .. seealso:: :ref:`tutorial/function`

.. release:: 0.2.1
    :date: 2023-01-20

    .. change:: fixed

        Updated configuration to include custom backend script in Python
        distribution.

    .. change:: fixed

        Fixed incorrect CMake functions in documentation.

.. release:: 0.2.0
    :date: 2023-01-20

    .. change:: changed

        Added custom build backend to ensure compatibility with Python 2.7.

.. release:: 0.1.0
    :date: 2022-12-13

    .. change:: new

        Initial release with the :term:`Pip` package manager.
