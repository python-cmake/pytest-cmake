import os

import pytest_cmake._dll_directories as plugin


def test_registers_existing_directories(tmp_path, monkeypatch):
    """Register every existing directory listed in the environment."""
    existing1 = tmp_path / "one"
    existing2 = tmp_path / "two"
    existing1.mkdir()
    existing2.mkdir()
    missing = tmp_path / "missing"

    registered = []
    monkeypatch.setattr(
        os, "add_dll_directory",
        lambda path: registered.append(path) or object(),
        raising=False,
    )
    monkeypatch.setenv(
        "PYTEST_CMAKE_DLL_DIRECTORIES",
        os.pathsep.join([str(existing1), str(missing), str(existing2)]),
    )

    monkeypatch.setattr(plugin, "_HANDLES", [])
    plugin._register_dll_directories()

    # The missing directory is skipped and the handles are kept alive.
    assert registered == [str(existing1), str(existing2)]
    assert len(plugin._HANDLES) == 2


def test_noop_when_env_is_empty(monkeypatch):
    """Do nothing when no directory is provided."""
    registered = []
    monkeypatch.setattr(
        os, "add_dll_directory",
        lambda path: registered.append(path) or object(),
        raising=False,
    )
    monkeypatch.delenv("PYTEST_CMAKE_DLL_DIRECTORIES", raising=False)

    monkeypatch.setattr(plugin, "_HANDLES", [])
    plugin._register_dll_directories()

    assert registered == []
    assert plugin._HANDLES == []


def test_noop_without_add_dll_directory(tmp_path, monkeypatch):
    """Do nothing where os.add_dll_directory is unavailable (non-Windows)."""
    existing = tmp_path / "one"
    existing.mkdir()

    monkeypatch.delattr(os, "add_dll_directory", raising=False)
    monkeypatch.setenv("PYTEST_CMAKE_DLL_DIRECTORIES", str(existing))

    monkeypatch.setattr(plugin, "_HANDLES", [])
    plugin._register_dll_directories()

    assert plugin._HANDLES == []
