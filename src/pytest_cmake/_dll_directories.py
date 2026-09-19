"""Pytest plugin registering native DLL search directories on Windows.

Since Python 3.8, ``PATH`` is no longer searched to resolve the DLL
dependencies of extension modules on Windows, so this plugin calls
:func:`os.add_dll_directory` for each directory listed in the
``PYTEST_CMAKE_DLL_DIRECTORIES`` environment variable (``os.pathsep``
separated). It is wired up by the CMake integration on Windows and is a no-op
elsewhere, where :func:`os.add_dll_directory` does not exist.
"""

import os

#: Keep the directory handles alive so the directories stay on the search path.
_HANDLES = []


def _register_dll_directories():
    """Register each directory from the environment for DLL resolution."""
    add_dll_directory = getattr(os, "add_dll_directory", None)
    if add_dll_directory is None:
        return

    raw = os.environ.get("PYTEST_CMAKE_DLL_DIRECTORIES", "")
    for path in raw.split(os.pathsep):
        if path and os.path.isdir(path):
            _HANDLES.append(add_dll_directory(path))


# Register at import time, before any test module imports its extension.
_register_dll_directories()
