from .calculator import calculator

import pytest

def test_calculate_payment_fee_with_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_with_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_with_small_positive_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_with_large_positive_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_with_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_payment_fee_with_small_negative_amount():
    assert calculate_payment_fee(-0.01) == -0.0103

def test_calculate_payment_fee_with_large_negative_amount():
    assert calculate_payment_fee(-1000000.0) == -1030000.0

def test_calculate_payment_fee_with_edge_case_positive_amount():
    assert calculate_payment_fee(0.000001) == 1.03e-06

def test_calculate_payment_fee_with_edge_case_negative_amount():
    assert calculate_payment_fee(-0.000001) == -1.03e-06

def test_calculate_payment_fee_with_minimal_amount():
    assert calculate_payment_fee(1e-10) == 1.03e-10
