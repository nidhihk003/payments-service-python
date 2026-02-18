from .src.payments.discounts import discounts

import pytest

def test_apply_discount_within_valid_range():
    assert apply_discount(100.0, 20.0) 

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -10.0)

def test_apply_discount_percentage_greater_than_100():
    with pytest.raises(ValueError):
        apply_discount(100.0, 110.0)

def test_apply_discount_minimal_amount():
    assert apply_discount(0.01, 50.0) == 0.005

def test_apply_discount_large_amount():
    assert apply_discount(1000000.0, 10.0) == 900000.0

def test_apply_discount_fractional_percentage():
    assert apply_discount(100.0, 12.5) == 87.5

def test_apply_discount_boundary_percentage():
    assert apply_discount(100.0, 99.99) == 0.010000000000005116

def test_apply_discount_no_discount():
    assert apply_discount(100.0, 0) == 100.0
