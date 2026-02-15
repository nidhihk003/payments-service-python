def test_calculate_payment_fee_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-100.0) == -103.0

def test_apply_discount_valid_percentage():
    assert apply_discount(100.0, 20.0) == 80.0

def test_apply_discount_zero_percentage():
    assert apply_discount(100.0, 0.0) == 100.0

def test_apply_discount_invalid_negative_percentage():
    assert apply_discount(100.0, -10.0) == {'exception': {'name': 'ValueError', 'message': 'Invalid discount'}}

def test_apply_discount_invalid_over_100_percentage():
    assert apply_discount(100.0, 110.0) == {'exception': {'name': 'ValueError', 'message': 'Invalid discount'}}

def test_process_payment_success():
    assert PaymentProcessor().process_payment('user123', Decimal('100.0'), 'USD', 'card') == {'status': 'SUCCESS'}

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment('user123', Decimal('-100.0'), 'USD', 'card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_unsupported_currency():
    assert PaymentProcessor().process_payment('user123', Decimal('100.0'), 'GBP', 'card') == {'exception': {'name': 'ValueError', 'message': 'Unsupported currency'}}

def test_process_payment_unsupported_method():
    assert PaymentProcessor().process_payment('user123', Decimal('100.0'), 'USD', 'bank_transfer') == {'exception': {'name': 'PaymentError', 'message': 'Payment failed at gateway'}}
