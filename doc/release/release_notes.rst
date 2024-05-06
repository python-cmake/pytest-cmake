.. _release/release_notes:

*************
Release Notes
*************

.. release:: Upcoming

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

        .. seealso:: :ref:`getting_started/function`

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
