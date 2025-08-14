import random

def test_random():
    assert random.choice([1, 2, 3]) in (1, 2, 3)
