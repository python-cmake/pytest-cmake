# -*- coding: utf-8 -*-

import example


def test_greet_world():
    """Greet the world."""
    assert example.greet() == "hello, world"


def test_greet_john():
    """Greet John."""
    assert example.greet("John") == "hello, John"


def test_greet_julia():
    """Greet Julia."""
    assert example.greet("Julia") == "hello, Julia"


def test_greet_julia_french(monkeypatch):
    """Greet Julia in French."""
    monkeypatch.delenv("GREETING_WORD")
    assert example.greet("Julia") == "bonjour, Julia"

