from .discounts import discounts

import pytest

def test_apply_discount_with_valid_percentage():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_with_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_with_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_with_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5.0)

def test_apply_discount_with_percentage_greater_than_100():
    with pytest.raises(ValueError):
        apply_discount(100.0, 105.0)

def test_apply_discount_with_minimal_positive_percentage():
    assert apply_discount(100.0, 0.01) == 99.99

def test_apply_discount_with_minimal_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -0.01)

def test_apply_discount_with_large_amount_and_valid_percentage():
    assert apply_discount(1000000.0, 50.0) == 500000.0

def test_apply_discount_with_fractional_percentage():
    assert apply_discount(250.0, 12.5) == 218.75

def test_apply_discount_with_free_item():
    assert apply_discount(0.0, 50.0) == 0.0

def test_apply_discount_with_negative_amount_and_valid_percentage():
    assert apply_discount(-100.0, 20.0) == -80.0

def test_apply_discount_with_negative_amount_and_zero_percentage():
    assert apply_discount(-100.0, 0.0) == -100.0

def test_apply_discount_with_negative_amount_and_full_percentage():
    assert apply_discount(-100.0, 100.0) == 0.0

def test_apply_discount_with_minimal_positive_percentage_on_large_amount():
    assert apply_discount(1000000.0, 0.01) == 999900.0

def test_apply_discount_with_fractional_percentage_on_large_amount():
    assert apply_discount(1000000.0, 12.5) == 875000.0
