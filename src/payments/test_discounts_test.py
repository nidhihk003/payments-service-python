def test_apply_discount_valid_percentage():
    assert apply_discount(100, 10) == 90.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100, 0) == 100.0

def test_apply_discount_hundred_percentage():
    assert apply_discount(100, 100) == 0.0

def test_apply_discount_negative_percentage():
    assert apply_discount(100, -10) == ValueError: Invalid discount

def test_apply_discount_percentage_greater_than_100():
    assert apply_discount(100, 110) == ValueError: Invalid discount

def test_apply_discount_zero_amount():
    assert apply_discount(0, 50) == 0.0

def test_apply_discount_large_amount():
    assert apply_discount(1000000, 25) == 750000.0

def test_apply_discount_edge_case_just_below_100_percentage():
    assert apply_discount(100, 99.999) == 0.001

def test_apply_discount_edge_case_just_above_0_percentage():
    assert apply_discount(100, 0.001) == 99.999

def test_apply_discount_minimum_float_amount():
    assert apply_discount(0.0001, 50) == 5e-05
