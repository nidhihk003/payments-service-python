from .discounts import discounts

import pytest

def test_apply_discount_zero_amount():
    assert apply_discount(0.0, 10.0) == 0.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_negative_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, -1.0)

def test_apply_discount_over_100_percentage():
    with pytest.raises(ValueError):
        apply_discount(100.0, 101.0)

def test_apply_discount_boundary_percentage_100():
    assert apply_discount(50.0, 100.0) == 0.0

def test_apply_discount_boundary_percentage_0():
    assert apply_discount(50.0, 0.0) == 50.0

def test_apply_discount_edge_case_just_above_0():
    assert apply_discount(50.0, 0.0001) == 49.99995

def test_apply_discount_edge_case_just_below_100():
    assert apply_discount(50.0, 99.9999) == 5.000000025492957e-05

def test_apply_discount_typical_case():
    assert apply_discount(200.0, 25.0) == 150.0
