from .src.payments.discounts import discounts

import pytest

def test_apply_discount_with_null_amount():
    with pytest.raises(TypeError):
        apply_discount(None, 20.0)

def test_apply_discount_with_null_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, None)

def test_apply_discount_with_empty_amount():
    with pytest.raises(TypeError):
        apply_discount('', 20.0)

def test_apply_discount_with_empty_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, '')

def test_apply_discount_with_string_amount():
    with pytest.raises(TypeError):
        apply_discount('100', 20.0)

def test_apply_discount_with_string_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, '20')

def test_apply_discount_with_large_amount():
    assert apply_discount(1e18, 50.0) == 5e+17

def test_apply_discount_with_large_percentage():
    assert apply_discount(100.0, 99.99) == 0.01

def test_apply_discount_with_minimal_non_zero_amount_and_percentage():
    assert apply_discount(0.01, 0.001) == 0.0099999

def test_apply_discount_with_large_amount_and_minimal_non_zero_percentage():
    assert apply_discount(1e18, 0.00001) == 999999999999900.0
