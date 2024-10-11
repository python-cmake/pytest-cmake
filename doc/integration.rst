.. _integration:

**********************
Integrating with CMake
**********************

.. highlight:: bash

Once :ref:`installed <installing>`, the package integration within a
:term:`CMake` project can be done using the :term:`find_package` function:

.. code-block:: cmake

    find_package(Pytest)

A specific range of versions can be targeted:

.. code-block:: cmake

    # Request Pytest version 7.2.0.
    find_package(Pytest 7.2.0 EXACT REQUIRED)

    # Request Pytest between version 6.0.0 and 7.2.0 included.
    find_package(Pytest 6.0.0...7.2.0 REQUIRED)

    # Request any version of Pytest over 4.6.11.
    find_package(Pytest 4.6.11 REQUIRED)

.. _integration/config:

Finding Configuration
=====================

When Python is used from its standard system location, :term:`CMake` should be
able to discover the newly installed configuration automatically using its
`Config Mode Search Procedure
<https://cmake.org/cmake/help/latest/command/find_package.html#search-procedure>`_.

.. warning::

    The `CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH
    <https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH.html>`_
    option should not be set to False.

When using a Python virtual environment, or if Python is installed in a
non-standard location, the :envvar:`Pytest_ROOT` environment variable
(or :term:`CMake` option) can be used to guide the discovery process::

    cmake -S . -B ./build -D "Pytest_ROOT=/path/to/python/prefix"

This is also necessary when installing the configuration in the
`Python user directory
<https://pip.pypa.io/en/stable/cli/pip_install/#install-user>`_::

    pip install pytest-cmake --user

.. _integration/config/example:

Building and testing example project
------------------------------------

An example project has been made available to test the configuration.

Ensure that :term:`nanobind` is available, and install :term:`Pytest` with its
:term:`CMake` configuration as described in the :ref:`previous section <installing>`.
Then build the example::

    export nanobind_ROOT=$(python -m nanobind --cmake_dir)
    cmake -S ./example -B ./build
    cmake --build ./build

Finally, run the tests as follows::

    ctest --test-dir ./build -VV

.. _integration/module:

Finding Module
==============

The package integration within a :term:`CMake` project can also be done using
the :file:`FindPytest.cmake` module. The CMake files can be copied into a
new project, or the following code can be added before invoking the
:term:`find_package` function:

.. code-block:: cmake

    set(pytest_url https://github.com/python-cmake/pytest-cmake/archive/main.zip)

    # Fetch CMake files from the main branch of the Github repository
    file(DOWNLOAD ${pytest_url} ${CMAKE_BINARY_DIR}/pytest.zip)
    file(
        ARCHIVE_EXTRACT INPUT ${CMAKE_BINARY_DIR}/pytest.zip
        DESTINATION ${CMAKE_BINARY_DIR}
        PATTERNS "*.cmake"
    )

    # Expand the module path variable to discover the `FindPytest.cmake` module.
    set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_BINARY_DIR}/pytest-cmake-main/cmake)

.. warning::

    It is strongly recommended to use the :term:`Pip` installation over
    this method.

