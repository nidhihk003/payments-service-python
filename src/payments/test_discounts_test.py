def test_apply_discount_with_valid_percentage():
    assert apply_discount(100, 20) == 80.0

def test_apply_discount_with_zero_percentage():
    assert apply_discount(100, 0) == 100.0

def test_apply_discount_with_full_percentage():
    assert apply_discount(100, 100) == 0.0

def test_apply_discount_with_negative_percentage():
    assert apply_discount(100, -10) == ValueError('Invalid discount')

def test_apply_discount_with_percentage_greater_than_100():
    assert apply_discount(100, 110) == ValueError('Invalid discount')

def test_apply_discount_with_small_amount():
    assert apply_discount(0.01, 50) == 0.005

def test_apply_discount_with_large_amount():
    assert apply_discount(1000000, 10) == 900000.0

def test_apply_discount_with_edge_case_percentage_0():
    assert apply_discount(100, 0) == 100.0

def test_apply_discount_with_edge_case_percentage_100():
    assert apply_discount(100, 100) == 0.0

def test_apply_discount_with_high_precision_amount():
    assert apply_discount(100.123456, 10) == 90.1111104
