def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100) == 0.0

def test_apply_discount_half_percentage():
    assert apply_discount(100.0, 50) == 50.0

def test_apply_discount_typical_case():
    assert apply_discount(200.0, 25) == 150.0

def test_apply_discount_float_percentage():
    assert apply_discount(100.0, 33.33) == 66.67

def test_apply_discount_negative_percentage():
    assert apply_discount(100.0, -5) == ValueError("Invalid discount")

def test_apply_discount_percentage_over_100():
    assert apply_discount(100.0, 105) == ValueError("Invalid discount")

def test_apply_discount_zero_amount():
    assert apply_discount(0, 50) == 0.0

def test_apply_discount_large_amount():
    assert apply_discount(1000000.0, 10) == 900000.0

def test_apply_discount_small_amount():
    assert apply_discount(0.01, 50) == 0.005
