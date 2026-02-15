def test_process_payment_valid_card_payment():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), 'USD', 'card') == {'transaction_id': 'txn-', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime', 'gateway_ref': 'reference'}

def test_process_payment_valid_wallet_payment():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), 'USD', 'wallet') == {'transaction_id': 'txn-', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime', 'gateway_ref': 'reference'}

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment('user123', Decimal('-100.00'), 'USD', 'card') == ValueError('Amount must be positive')

def test_process_payment_zero_amount():
    assert PaymentProcessor().process_payment('user123', Decimal('0.00'), 'USD', 'card') == ValueError('Amount must be positive')

def test_process_payment_unsupported_currency():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), 'GBP', 'card') == ValueError('Unsupported currency')

def test_process_payment_gateway_failure():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), 'USD', 'card') == PaymentError('Payment failed at gateway')

def test_process_payment_api_response_error():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), 'USD', 'card') == PaymentError('Gateway error: ')

def test_process_payment_invalid_user_id():
    assert PaymentProcessor().process_payment('', Decimal('100.00'), 'USD', 'card') == PaymentError('Payment failed at gateway')

def test_process_payment_large_amount():
    assert PaymentProcessor().process_payment('user123', Decimal('1000000000.00'), 'USD', 'card') == {'transaction_id': 'txn-', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime', 'gateway_ref': 'reference'}

def test_process_payment_inr_currency():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), 'INR', 'card') == {'transaction_id': 'txn-', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime', 'gateway_ref': 'reference'}
