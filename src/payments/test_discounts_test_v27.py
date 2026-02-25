from .discounts import discounts

import pytest

def test_apply_discount_within_valid_range():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_hundred_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -10.0)

def test_apply_discount_percentage_greater_than_hundred():
    with pytest.raises(ValueError):
        apply_discount(100.0, 150.0)

def test_apply_discount_edge_case_just_below_zero():
    with pytest.raises(ValueError):
        apply_discount(100.0, -0.01)

def test_apply_discount_edge_case_just_above_hundred():
    with pytest.raises(ValueError):
        apply_discount(100.0, 100.01)

def test_apply_discount_zero_amount():
    assert apply_discount(0.0, 50.0) == 0.0

def test_apply_discount_large_amount_small_percentage():
    assert apply_discount(1000000.0, 0.01) == 999900.0

def test_apply_discount_large_amount_large_percentage():
    assert apply_discount(1000000.0, 99.99) == 100.0

def test_apply_discount_edge_case_min_percentage():
    assert apply_discount(100.0, 0.01) == 99.99

def test_apply_discount_edge_case_max_amount():
    assert apply_discount(100.0, 99.99) == 0.01

def test_apply_discount_floating_point_precision():
    assert apply_discount(1.0, 33.3333) == 0.6666667

def test_apply_discount_negative_amount():
    assert apply_discount(-100.0, 20.0) == -80.0

def test_apply_discount_large_negative_amount():
    assert apply_discount(-1000000.0, 50.0) == -500000.0
