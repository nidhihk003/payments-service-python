def test_calculate_payment_fee_standard_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_large_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_payment_fee_minimal_positive_amount():
    assert calculate_payment_fee(0.0001) == 0.000103

def test_calculate_payment_fee_minimal_negative_amount():
    assert calculate_payment_fee(-0.0001) == -0.000103

def test_calculate_payment_fee_float_precision():
    assert calculate_payment_fee(1234.5678) == 1271.604834

def test_calculate_payment_fee_rounded_amount():
    assert calculate_payment_fee(50.05) == 51.5515

def test_calculate_payment_fee_max_float_amount():
    assert calculate_payment_fee(1.79e308) == inf
