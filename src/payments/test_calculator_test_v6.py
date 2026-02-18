from .calculator import calculator

import pytest

def test_calculate_payment_fee_with_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_with_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_with_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_with_large_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_with_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_payment_fee_with_decimal_amount():
    assert calculate_payment_fee(123.45) == 127.1435

def test_calculate_payment_fee_with_one():
    assert calculate_payment_fee(1.0) == 1.03

def test_calculate_payment_fee_with_max_float():
    assert calculate_payment_fee(1.7976931348623157e+308) == inf

def test_calculate_payment_fee_with_min_float():
    assert calculate_payment_fee(5e-324) == 5e-324

def test_calculate_payment_fee_with_fractional_cents():
    assert calculate_payment_fee(0.005) == 0.00515
