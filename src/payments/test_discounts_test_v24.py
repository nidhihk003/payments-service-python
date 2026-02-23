from .discounts import apply_discount

import pytest

def test_apply_discount_valid_discount():
    assert apply_discount(100.0, 10.0) == 90.0

def test_apply_discount_zero_discount():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_discount():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_negative_discount():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5.0)

def test_apply_discount_exceeding_discount():
    with pytest.raises(ValueError):
        apply_discount(100.0, 105.0)
