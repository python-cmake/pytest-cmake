import pytest

class TestStringMethods:

    def test_upper(self):
        assert "example".upper() == "EXAMPLE"

    def test_lower(self):
        assert "EXAMPLE".lower() == "example"

    def test_capitalize(self):
        assert "hello".capitalize() == "Hello"

    def test_split(self):
        s = "hello world"
        assert s.split() == ["hello", "world"]
        with pytest.raises(TypeError):
            s.split(2)
