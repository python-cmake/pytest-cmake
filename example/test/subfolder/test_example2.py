import foo

import pytest


def test_greet_michael():
    """Greet Michael."""
    assert foo.greet("Michael") == "hello, Michael"


def test_greet_error(monkeypatch):
    """Impossible to greet when FOO settings is not found."""
    monkeypatch.delenv("FOO_SETTINGS_FILE")

    with pytest.raises(RuntimeError) as error:
        foo.greet("Michael")

    assert "Environment variable FOO_SETTINGS_FILE is not set" in str(error.value)