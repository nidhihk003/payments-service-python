def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_large_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_calculate_payment_fee_edge_case_just_above_zero():
    assert calculate_payment_fee(0.000001) == 1.03e-06

def test_calculate_payment_fee_edge_case_just_below_threshold():
    assert calculate_payment_fee(999999.99) == 1029999.9897

def test_calculate_payment_fee_edge_case_just_above_threshold():
    assert calculate_payment_fee(1000000.01) == 1030000.0103

def test_calculate_payment_fee_rounding_check():
    assert calculate_payment_fee(33.33) == 34.3299

def test_calculate_payment_fee_high_precision_amount():
    assert calculate_payment_fee(12345.678901234567) == 12716.049268570605
