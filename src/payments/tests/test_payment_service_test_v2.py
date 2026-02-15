def test_calculate_payment_fee_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-50.0) == -51.5

def test_calculate_payment_fee_very_large_amount():
    assert calculate_payment_fee(1e18) == 1.03e+18

def test_apply_discount_valid_percentage():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_full_percentage():
    assert apply_discount(100.0, 100.0) == 0.0

def test_apply_discount_negative_percentage():
    assert apply_discount(100.0, -10.0) == {'exception': {'name': 'ValueError', 'message': 'Invalid discount'}}

def test_apply_discount_percentage_above_100():
    assert apply_discount(100.0, 150.0) == {'exception': {'name': 'ValueError', 'message': 'Invalid discount'}}

def test_process_payment_valid_input():
    assert PaymentProcessor().process_payment('user123', Decimal('100.0'), 'USD', 'card') == {'transaction_id': 'string', 'status': 'SUCCESS', 'processed_at': 'string', 'gateway_ref': 'string'}
