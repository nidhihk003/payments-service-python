from .src.payments.discounts import discounts

import pytest

def test_valid_discount():
    assert apply_discount(200.0, 20.0) == 160.0

def test_zero_discount():
    assert apply_discount(100.0, 0.0) == 100.0

def test_full_discount():
    assert apply_discount(50.0, 100.0) == 0.0

def test_no_discount():
    assert apply_discount(75.0, 0.0) == 75.0

def test_negative_discount_percentage():
    with pytest.raises(ValueError):
        apply_discount(150.0, -10.0)

def test_over_100_discount_percentage():
    with pytest.raises(ValueError):
        apply_discount(300.0, 150.0)

def test_minimum_amount_with_valid_discount():
    assert apply_discount(0.01, 50.0) == 0.005

def test_minimum_amount_with_no_discount():
    assert apply_discount(0.01, 0.0) == 0.01

def test_high_amount_with_valid_discount():
    assert apply_discount(1000000.0, 25.0) == 750000.0

def test_high_amount_with_no_discount():
    assert apply_discount(1000000.0, 0.0) == 1000000.0
