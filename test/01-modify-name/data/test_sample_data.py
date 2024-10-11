import pytest

def test_inventory_keys(sample_data):
    for fruit in sample_data:
        assert "quantity_in_stock" in sample_data[fruit]

def test_inventory_values(sample_data):
    for fruit, data in sample_data.items():
        assert isinstance(data["quantity_in_stock"], int)
        assert data["quantity_in_stock"] > 0

@pytest.mark.parametrize("fruit, expected_quantity", [
    ("banana", 150),
    ("apple", 100),
    ("orange", 200),
], ids=["Fruit[banana]=150", "Fruit[apple]=100", "Fruit[orange]=200"])
def test_fruit_quantity(sample_data, fruit, expected_quantity):
    assert sample_data[fruit]["quantity_in_stock"] == expected_quantity
