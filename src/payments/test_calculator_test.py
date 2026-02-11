def test_calculate_payment_fee_normal_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_high_amount():
    assert calculate_payment_fee(1000000.0) == 1030000.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-50.0) == -51.5

def test_calculate_payment_fee_boundary_positive_amount():
    assert calculate_payment_fee(0.0001) == 0.000103

def test_calculate_payment_fee_boundary_negative_amount():
    assert calculate_payment_fee(-0.0001) == -0.000103

def test_calculate_payment_fee_large_float_amount():
    assert calculate_payment_fee(1e10) == 10300000000.0

def test_calculate_payment_fee_small_negative_amount():
    assert calculate_payment_fee(-0.01) == -0.0103

def test_calculate_payment_fee_typical_business_amount():
    assert calculate_payment_fee(500.75) == 515.7725
