def test_apply_standard_discount():
    assert apply_discount(100.0, 10.0) == 90.0

def test_apply_no_discount():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_full_discount():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_minimal_discount():
    assert apply_discount(100.0, 0.01) == 99.99

def test_apply_maximal_valid_discount():
    assert apply_discount(100.0, 99.99) == 0.010000000000005116

def test_negative_discount_percentage():
    assert apply_discount(100.0, -1.0) == ValueError('Invalid discount')

def test_greater_than_100_discount_percentage():
    assert apply_discount(100.0, 101.0) == ValueError('Invalid discount')

def test_apply_discount_with_large_amount():
    assert apply_discount(1000000.0, 15.0) == 850000.0

def test_apply_discount_to_small_amount():
    assert apply_discount(0.01, 50.0) == 0.005

def test_apply_discount_with_high_precision():
    assert apply_discount(1234.56789, 12.345) == 1082.05447405
