.. _installing:

**********
Installing
**********

.. highlight:: bash

The :term:`CMake` configuration can be easily installed alongside :term:`Pytest`
using :term:`Pip`::

    pip install pytest pytest-cmake

The :term:`find_package` function will be used to integrate the package within
a :term:`CMake` project.

.. code-block:: cmake

    find_package(Pytest)

The package discovery relies on the `Config Mode Search Procedure
<https://cmake.org/cmake/help/latest/command/find_package.html#search-procedure>`_.
Configuration files should be found under the system environment path at the
following path::

    <PYTHON_ROOT>/share/Pytest/cmake

.. warning::

    The `CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH
    <https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH.html#variable:CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH>`_
    variable should not be set to False.

.. _installing/source:

Installing from source
======================

You can also install the configuration manually from the source for more
control. First, obtain a copy of the source by either downloading the
`zipball <https://github.com/python-cmake/pytest-cmake/archive/main.zip>`_ or
cloning the public repository::

    git clone git@github.com:python-cmake/pytest-cmake.git

Then you can build and install the package into your current Python
environment::

    pip install .

.. note::

    The project can not be installed in `editable mode
    <https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs>`_
    as :term:`CMake` files won't be accessible.

.. _installing/source/doc:

Building documentation from source
----------------------------------

Ensure you have installed the dependencies required for building the
documentation::

    pip install -r ./doc/requirements.txt

Then you can build the documentation with the command::

    sphinx-build ./doc ./build/doc/html

View the result in your browser at::

    file:///path/to/pytest-build/build/doc/html/index.html

.. _installing/source/test:

Running tests against the source
--------------------------------

An example project has been made available to test the configuration.

Ensure that a minimal version of :term:`Boost Python` is available, and
install :term:`Pytest` with its :term:`CMake` configuration as described in the
previous section. Then build the example::

    cmake -S ./example -B ./build
    cmake --build ./build

Finally, run the tests as follows::

    ctest --test-dir ./build -VV

.. _installing/module:

Installing in Module mode
=========================

The package integration within a :term:`CMake` project can also be done in
module mode. The CMake files can be copied into a new project, or the following
code can be added before invoking the :term:`find_package` function:

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

.. note::

    It is recommended to use the :term:`Pip` installation over this method.
