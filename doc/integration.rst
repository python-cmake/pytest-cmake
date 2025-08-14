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

When using a Python virtual environment, installing Python in a non-standard location, or
installing ``pytest-cmake`` in the `Python user directory
<https://pip.pypa.io/en/stable/cli/pip_install/#install-user>`_, specify the ``Pytest_ROOT``
path via the CLI::

    cmake -S . -B ./build -D "Pytest_ROOT=$(python -m pytest_cmake --cmake-dir)"

.. _integration/config/example:

Building and testing example project
------------------------------------

An example project has been made available to test the configuration.

Ensure that :term:`nanobind` is available, and install :term:`Pytest` with its
:term:`CMake` configuration as described in the :ref:`previous section <installing>`.
Then build the example::

    cmake -S ./example -B ./build -D "nanobind_ROOT=$(python -m nanobind --cmake-dir)"
    cmake --build ./build

Finally, run the tests as follows::

    ctest --test-dir ./build -VV

