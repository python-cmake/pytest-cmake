.. _installing:

************************
Installing Configuration
************************

.. highlight:: bash

The :term:`CMake` configuration for the current :term:`Pytest` version can be
easily installed using :term:`Pip`::

    pip install pytest-cmake

.. note::

    :term:`Pytest` will be installed as a dependency if necessary.

The configuration files should be located in the Python installation prefix::

    <python_prefix>/share/Pytest/cmake

.. seealso:: :ref:`integration`

.. _installing/source:

Installing from source
======================

You can also install the configuration manually from the source for more
control. First, obtain a copy of the source by either downloading the
`zipball <https://github.com/python-cmake/pytest-cmake/archive/main.zip>`_ or
cloning the public repository::

    git clone git@github.com:python-cmake/pytest-cmake.git

Then build and install the package into your current Python environment::

    pip install .

.. note::

    The project can not be installed in `editable mode
    <https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs>`_
    as package data won't be installed.

.. _installing/source/doc:

Building documentation from source
----------------------------------

Ensure you have installed the dependencies required for building the
documentation::

    pip install -r ./doc/requirements.txt

Then, build the documentation with the command::

    sphinx-build ./doc ./build/doc/html

View the result in your browser at::

    file:///path/to/sphinx-build/build/doc/html/index.html

.. _installing/deployment:

Package Deployment
==================

This package is deployed as a source on `PyPi <https://pypi.org/project/pytest-cmake/>`_
to allow dynamic adaptation of :term:`CMake` scripts based on the version of :term:`Pytest`
available at installation. Packaging it as a
`wheel <https://packaging.python.org/en/latest/specifications/binary-distribution-format>`_
would lock the :term:`Pytest` version detected during the packaging and deployment process,
reducing flexibility and compatibility with future versions.

If you wish to deploy the package as a source within a custom index, it is important to include
the build requirements in your environment (e.g. "hatchling" and "cmake").

.. seealso:: `Package Formats <https://packaging.python.org/en/latest/discussions/package-formats>`_
