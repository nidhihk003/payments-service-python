from .discounts import discounts

import pytest

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_half_percentage():
    assert apply_discount(100.0, 50.0) == 50.0

def test_apply_discount_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -10.0)

def test_apply_discount_above_hundred_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, 110.0)

def test_apply_discount_edge_case_near_zero_amount():
    assert apply_discount(0.01, 50.0) == 0.005

def test_apply_discount_edge_case_large_amount():
    assert apply_discount(1000000.0, 25.0) == 750000.0

def test_apply_discount_edge_case_min_discount():
    assert apply_discount(100.0, 0.0001) == 99.9999

def test_apply_discount_edge_case_max_discount_without_error():
    assert apply_discount(100.0, 99.9999) == 0.0001

def test_apply_discount_edge_case_just_over_max_discount():
    with pytest.raises(ValueError):
        apply_discount(100.0, 100.0001)
