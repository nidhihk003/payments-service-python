def test_apply_discount_within_valid_range():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_boundary_negative_percentage():
    assert apply_discount(100.0, -0.01) == raises ValueError

def test_apply_discount_boundary_above_100_percentage():
    assert apply_discount(100.0, 100.01) == raises ValueError

def test_apply_discount_exactly_zero_amount():
    assert apply_discount(0.0, 20.0) == 0.0

def test_apply_discount_large_amount_small_percentage():
    assert apply_discount(1000000.0, 0.0001) == 999999.0

def test_apply_discount_large_amount_large_percentage():
    assert apply_discount(1000000.0, 99.9999) == 1.0

def test_apply_discount_minimal_non_zero_amount():
    assert apply_discount(0.01, 50.0) == 0.005

def test_apply_discount_max_float_amount():
    assert apply_discount(1.7976931348623157e+308, 50.0) == 8.988465674311579e+307
