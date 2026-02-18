from .src.payments.discounts import unknown_function

import pytest

def test_apply_discount_with_valid_percentage():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_with_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_with_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_with_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -10.0)

def test_apply_discount_with_percentage_over_100():
    with pytest.raises(ValueError):
        apply_discount(100.0, 110.0)

def test_apply_discount_with_minimal_amount():
    assert apply_discount(0.01, 50.0) == 0.005

def test_apply_discount_with_zero_amount():
    assert apply_discount(0.0, 50.0) == 0.0

def test_apply_discount_with_large_amount():
    assert apply_discount(1000000.0, 25.0) == 750000.0

def test_apply_discount_with_float_percentage():
    assert apply_discount(100.0, 33.33) == 66.67

def test_apply_discount_with_high_precision():
    assert apply_discount(1234.5678, 12.3456) == 1082.06221312
