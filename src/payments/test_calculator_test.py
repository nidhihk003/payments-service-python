def test_calculate_payment_fee_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_large_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_payment_fee_boundary_positive():
    assert calculate_payment_fee(1.0) == 1.03

def test_calculate_payment_fee_boundary_negative():
    assert calculate_payment_fee(-1.0) == -1.03

def test_calculate_payment_fee_edge_case_very_large_amount():
    assert calculate_payment_fee(1e18) == 1.03e+18

def test_calculate_payment_fee_edge_case_very_small_amount():
    assert calculate_payment_fee(1e-18) == 1.03e-18

def test_calculate_payment_fee_edge_case_just_below_one():
    assert calculate_payment_fee(0.999999999) == 1.02999999897
