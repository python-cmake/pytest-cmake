import foo


def test_greet_world():
    """Greet the world."""
    assert foo.greet() == "hello, world"


def test_greet_john():
    """Greet John."""
    assert foo.greet("John") == "hello, John"


def test_greet_julia():
    """Greet Julia."""
    assert foo.greet("Julia") == "hello, Julia"


def test_greet_julia_french(monkeypatch):
    """Greet Julia in French."""
    monkeypatch.delenv("DEFAULT_LANGUAGE")
    assert foo.greet("Julia") == "bonjour, Julia"


def test_greet_julia_spanish(monkeypatch):
    """Greet Julia in Spanish."""
    monkeypatch.setenv("DEFAULT_LANGUAGE", "es")
    assert foo.greet("Julia") == "hola, Julia"
