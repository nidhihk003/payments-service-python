def test_calculate_payment_fee_with_small_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_with_large_positive_amount():
    assert calculate_payment_fee(10000.0) == 10300.0

def test_calculate_payment_fee_with_exact_one():
    assert calculate_payment_fee(1.0) == 1.03

def test_calculate_payment_fee_with_zero():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_with_small_decimal_amount():
    assert calculate_payment_fee(0.99) == 1.0197

def test_calculate_payment_fee_with_negative_amount():
    assert calculate_payment_fee(-50.0) == -51.5

def test_calculate_payment_fee_with_small_negative_decimal_amount():
    assert calculate_payment_fee(-0.99) == -1.0197

def test_calculate_payment_fee_with_rounding_required():
    assert calculate_payment_fee(123.456) == 127.15968

def test_calculate_payment_fee_with_large_decimal_amount():
    assert calculate_payment_fee(7890.12345) == 8126.8276545

def test_calculate_payment_fee_with_very_small_positive_amount():
    assert calculate_payment_fee(0.0001) == 0.000103
