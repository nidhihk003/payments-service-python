def test_apply_discount_valid_percentage():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_negative_percentage():
    assert apply_discount(100.0, -5.0) == ValueError('Invalid discount')

def test_apply_discount_more_than_100_percentage():
    assert apply_discount(100.0, 105.0) == ValueError('Invalid discount')

def test_apply_discount_large_amount():
    assert apply_discount(1000000.0, 10.0) == 900000.0

def test_apply_discount_small_amount():
    assert apply_discount(1.0, 50.0) == 0.5

def test_apply_discount_boundary_percentage_100():
    assert apply_discount(50.0, 100.0) == 0.0

def test_apply_discount_boundary_percentage_0():
    assert apply_discount(50.0, 0.0) == 50.0

def test_apply_discount_invalid_amount_type():
    assert apply_discount('100.0', 20.0) == TypeError
