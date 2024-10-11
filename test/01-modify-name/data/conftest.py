import pytest

@pytest.fixture
def sample_data():
    return {
        "banana": {"quantity_in_stock": 150},
        "apple": {"quantity_in_stock": 100},
        "orange": {"quantity_in_stock": 200}
    }
