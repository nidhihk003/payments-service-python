def test_apply_standard_discount():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_zero_discount():
    assert apply_discount(200.0, 0.0) == 200.0

def test_apply_full_discount():
    assert apply_discount(150.0, 100.0) == 0.0

def test_apply_partial_discount():
    assert apply_discount(50.0, 50.0) == 25.0

def test_apply_small_discount():
    assert apply_discount(10.0, 1.0) == 9.9

def test_invalid_negative_discount():
    assert apply_discount(100.0, -5.0) == ValueError('Invalid discount')

def test_invalid_excessive_discount():
    assert apply_discount(100.0, 150.0) == ValueError('Invalid discount')

def test_apply_discount_high_boundary():
    assert apply_discount(100.0, 99.99) == 0.010000000000005116

def test_apply_discount_low_boundary():
    assert apply_discount(100.0, 0.01) == 99.99

def test_apply_discount_no_amount():
    assert apply_discount(0.0, 50.0) == 0.0
