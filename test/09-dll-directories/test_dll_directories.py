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


class _FakeReport:
    def __init__(self, longrepr):
        self.longrepr = longrepr


class _FakeTerminalReporter:
    def __init__(self, stats):
        self.stats = stats
        self.lines = []

    def write_sep(self, sep, title, **kwargs):
        self.lines.append(title)

    def write_line(self, line, **kwargs):
        self.lines.append(line)


def test_summary_reports_directories_on_dll_error(monkeypatch):
    """List the registered directories when a DLL fails to load."""
    monkeypatch.setattr(plugin, "_DIRECTORIES", ["C:/libs/foo", "C:/libs/bar"])
    reporter = _FakeTerminalReporter(
        {"error": [_FakeReport("ImportError: DLL load failed while importing foo")]}
    )

    plugin.pytest_terminal_summary(reporter)

    output = "\n".join(reporter.lines)
    assert "C:/libs/foo" in output
    assert "C:/libs/bar" in output
    assert "LIBRARY_PATH_PREPEND" in output


def test_summary_silent_without_dll_error(monkeypatch):
    """Stay quiet when no DLL load failure is reported."""
    monkeypatch.setattr(plugin, "_DIRECTORIES", ["C:/libs/foo"])
    reporter = _FakeTerminalReporter(
        {"failed": [_FakeReport("AssertionError: 1 != 2")]}
    )

    plugin.pytest_terminal_summary(reporter)

    assert reporter.lines == []
