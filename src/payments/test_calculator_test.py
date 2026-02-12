def test_calculate_payment_fee_happy_path():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_large_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_payment_fee_edge_case_min_positive():
    assert calculate_payment_fee(1e-10) == 1.03e-10

def test_calculate_payment_fee_edge_case_max_float():
    assert calculate_payment_fee(1.79e308) == inf

def test_calculate_payment_fee_input_as_integer():
    assert calculate_payment_fee(50) == 51.5

def test_calculate_payment_fee_input_as_string():
    assert calculate_payment_fee('100.0') == TypeError

def test_calculate_payment_fee_none_input():
    assert calculate_payment_fee(None) == TypeError
