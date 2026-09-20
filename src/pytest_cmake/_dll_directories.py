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

#: Directories effectively registered, reported when a DLL fails to load.
_DIRECTORIES = []


def _register_dll_directories():
    """Register each directory from the environment for DLL resolution."""
    add_dll_directory = getattr(os, "add_dll_directory", None)
    if add_dll_directory is None:
        return

    raw = os.environ.get("PYTEST_CMAKE_DLL_DIRECTORIES", "")
    for path in raw.split(os.pathsep):
        if path and os.path.isdir(path):
            _DIRECTORIES.append(path)
            _HANDLES.append(add_dll_directory(path))


def pytest_terminal_summary(terminalreporter):
    """Explain "DLL load failed" errors with the registered directories.

    Windows does not name the missing dependency in the error, so list the
    directories that were searched and how to extend them.
    """
    reports = (
        terminalreporter.stats.get("error", [])
        + terminalreporter.stats.get("failed", [])
    )
    if not any("DLL load failed" in str(report.longrepr) for report in reports):
        return

    terminalreporter.write_sep("=", "pytest-cmake DLL resolution", yellow=True)
    if _DIRECTORIES:
        terminalreporter.write_line(
            "A native dependency was not found in the registered directories:"
        )
        for path in _DIRECTORIES:
            terminalreporter.write_line("  {}".format(path))
    else:
        terminalreporter.write_line("No DLL search directories were registered.")
    terminalreporter.write_line(
        "Expose the missing dependency through the LIBRARY_PATH_PREPEND or "
        "DEPENDS argument of pytest_discover_tests() (resolving DLL "
        "directories from DEPENDS requires CMake 3.27 or later)."
    )


# Register at import time, before any test module imports its extension.
_register_dll_directories()
