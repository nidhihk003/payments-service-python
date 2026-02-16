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

def test_calculate_payment_fee_with_non_integer_amount():
    assert calculate_payment_fee(123.45) == 127.1435

def test_calculate_payment_fee_with_round_number():
    assert calculate_payment_fee(50.0) == 51.5

def test_calculate_payment_fee_with_high_precision_amount():
    assert calculate_payment_fee(0.00001) == 1.03e-05

def test_calculate_payment_fee_with_boundary_amount():
    assert calculate_payment_fee(1.0) == 1.03

def test_calculate_payment_fee_with_negative_small_amount():
    assert calculate_payment_fee(-0.01) == -0.0103
