def test_calculate_payment_fee_happy_path():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_apply_discount_happy_path():
    assert apply_discount(100.0, 10.0) == 90.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_invalid_negative_percentage():
    assert apply_discount(100.0, -5.0) == {'exception': {'name': 'ValueError', 'message': 'Invalid discount'}}

def test_apply_discount_invalid_percentage_above_100():
    assert apply_discount(100.0, 105.0) == {'exception': {'name': 'ValueError', 'message': 'Invalid discount'}}

def test_process_payment_happy_path():
    assert PaymentProcessor().process_payment('user-123', Decimal('100.00'), 'USD', 'card') == {'transaction_id': 'txn-12345678', 'status': 'SUCCESS', 'processed_at': '2023-10-01T00:00:00', 'gateway_ref': 'gw-abcdef'}

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment('user-123', Decimal('-100.00'), 'USD', 'card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_unsupported_currency():
    assert PaymentProcessor().process_payment('user-123', Decimal('100.00'), 'JPY', 'card') == {'exception': {'name': 'ValueError', 'message': 'Unsupported currency'}}
