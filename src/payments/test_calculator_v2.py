def test_calculate_payment_fee_normal_amount():
    assert calculate_payment_fee(100.00) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.00) == 0.0

def test_calculate_payment_fee_small_amount():
    assert calculate_payment_fee(0.01) == 0.0103

def test_calculate_payment_fee_large_amount():
    assert calculate_payment_fee(1000000.00) == 1030000.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.00) == -103.0

def test_calculate_payment_fee_float_amount():
    assert calculate_payment_fee(123.45) == 127.1445

def test_calculate_payment_fee_edge_float_amount():
    assert calculate_payment_fee(0.0001) == 0.000103

def test_calculate_payment_fee_edge_large_float_amount():
    assert calculate_payment_fee(999999.99) == 1029999.9897

def test_calculate_payment_fee_edge_case_one():
    assert calculate_payment_fee(1.00) == 1.03

def test_calculate_payment_fee_edge_case_negative_one():
    assert calculate_payment_fee(-1.00) == -1.03

def test_calculate_payment_fee_small_negative_amount():
    assert calculate_payment_fee(-0.01) == -0.0103

def test_calculate_payment_fee_minimal_float_amount():
    assert calculate_payment_fee(1e-10) == 1.03e-10
