def test_calculate_payment_fee_standard_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_large_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_payment_fee_fractional_amount():
    assert calculate_payment_fee(123.45) == 127.1435

def test_calculate_payment_fee_boundary_amount():
    assert calculate_payment_fee(1.0) == 1.03

def test_calculate_payment_fee_very_large_amount():
    assert calculate_payment_fee(1e9) == 1030000000.0

def test_calculate_payment_fee_very_small_amount():
    assert calculate_payment_fee(1e-9) == 1.03e-09

def test_calculate_payment_fee_typical_amount():
    assert calculate_payment_fee(50.0) == 51.5
