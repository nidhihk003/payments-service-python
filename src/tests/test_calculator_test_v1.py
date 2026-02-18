from .payments.calculator import calculator

import pytest

def test_calculate_fee_with_standard_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_fee_with_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_fee_with_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_fee_with_large_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_fee_with_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_fee_with_minimum_float():
    assert calculate_payment_fee(1e-308) == 1.03e-308

def test_calculate_fee_with_maximum_float():
    assert calculate_payment_fee(1e+308) == 1.03e+308

def test_calculate_fee_with_subnormal_float():
    assert calculate_payment_fee(5e-324) == 5e-324

def test_calculate_fee_with_very_large_negative_amount():
    assert calculate_payment_fee(-1e+308) == -1.03e+308

def test_calculate_fee_with_edge_case_near_zero_positive():
    assert calculate_payment_fee(1e-10) == 1.03e-10
