from .discounts import discounts

import pytest

def test_apply_discount_with_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_with_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_with_half_percentage():
    assert apply_discount(100.0, 50.0) == 50.0

def test_apply_discount_with_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -1.0)

def test_apply_discount_with_percentage_above_100():
    with pytest.raises(ValueError):
        apply_discount(100.0, 101.0)

def test_apply_discount_with_minimum_non_zero_percentage():
    assert apply_discount(100.0, 0.01) == 99.99

def test_apply_discount_with_maximum_valid_percentage():
    assert apply_discount(100.0, 99.99) == 0.01

def test_apply_discount_with_zero_amount():
    assert apply_discount(0.0, 50.0) == 0.0

def test_apply_discount_with_large_amount_and_small_percentage():
    assert apply_discount(1000000.0, 0.5) == 995000.0

def test_apply_discount_with_large_amount_and_large_percentage():
    assert apply_discount(1000000.0, 99.5) == 5000.0
