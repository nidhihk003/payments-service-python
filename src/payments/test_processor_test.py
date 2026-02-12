def test_process_payment_valid_card_payment():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00')) == {'transaction_id': 'any-string', 'status': 'SUCCESS', 'processed_at': 'any-datetime', 'gateway_ref': 'any-string'}

def test_process_payment_valid_wallet_payment():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), payment_method='wallet') == {'transaction_id': 'any-string', 'status': 'SUCCESS', 'processed_at': 'any-datetime', 'gateway_ref': 'any-string'}

def test_process_payment_zero_amount():
    assert PaymentProcessor().process_payment('user123', Decimal('0.00')) == ValueError('Amount must be positive')

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment('user123', Decimal('-10.00')) == ValueError('Amount must be positive')

def test_process_payment_unsupported_currency():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), currency='JPY') == ValueError('Unsupported currency')

def test_process_payment_gateway_error():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00')) == PaymentError('Payment failed at gateway')

def test_process_payment_invalid_user_id():
    assert PaymentProcessor().process_payment('', Decimal('100.00')) == PaymentError('Payment failed at gateway')

def test_process_payment_invalid_amount_type():
    assert PaymentProcessor().process_payment('user123', '100.00') == TypeError

def test_process_payment_invalid_currency_type():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), currency=123) == ValueError('Unsupported currency')

def test_process_payment_invalid_payment_method():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), payment_method='cash') == PaymentError('Payment failed at gateway')
