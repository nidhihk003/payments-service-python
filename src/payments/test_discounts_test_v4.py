from .discounts import unknown_function

import pytest

def test_apply_discount_valid_percentage():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -10.0)

def test_apply_discount_percentage_over_100():
    with pytest.raises(ValueError):
        apply_discount(100.0, 110.0)

def test_apply_discount_minimum_positive_percentage():
    assert apply_discount(100.0, 0.01) == 99.99

def test_apply_discount_large_amount_small_discount():
    assert apply_discount(10000.0, 0.1) == 9990.0

def test_apply_discount_small_amount_large_discount():
    assert apply_discount(1.0, 99.0) == 0.01

def test_apply_discount_non_integer_percentage():
    assert apply_discount(200.0, 12.5) == 175.0

def test_apply_discount_zero_amount():
    assert apply_discount(0.0, 50.0) == 0.0
