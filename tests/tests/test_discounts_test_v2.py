def test_apply_discount_normal_case():
    assert apply_discount(100, 10) == 90.0

def test_apply_discount_zero_discount():
    assert apply_discount(100, 0) == 100.0

def test_apply_discount_full_discount():
    assert apply_discount(100, 100) == 0.0

def test_apply_discount_small_discount():
    assert apply_discount(50, 1) == 49.5

def test_apply_discount_large_amount():
    assert apply_discount(1000, 25) == 750.0

def test_apply_discount_percentage_edge_case_lower_bound():
    assert apply_discount(200, 0) == 200.0

def test_apply_discount_percentage_edge_case_upper_bound():
    assert apply_discount(200, 100) == 0.0

def test_apply_discount_percentage_below_zero():
    assert apply_discount(100, -1) == ValueError: Invalid discount

def test_apply_discount_percentage_above_hundred():
    assert apply_discount(100, 101) == ValueError: Invalid discount

def test_apply_discount_fractional_percentage():
    assert apply_discount(100, 33.33) == 66.67
