def test_process_payment_valid_card_payment():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card') == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime-object', 'gateway_ref': 'ref123'}

def test_process_payment_invalid_negative_amount():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('-10.00'), currency='USD', payment_method='card') == ValueError: Amount must be positive

def test_process_payment_invalid_zero_amount():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('0.00'), currency='USD', payment_method='card') == ValueError: Amount must be positive

def test_process_payment_invalid_currency():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='GBP', payment_method='card') == ValueError: Unsupported currency

def test_process_payment_valid_wallet_payment():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('50.00'), currency='USD', payment_method='wallet') == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime-object', 'gateway_ref': 'ref123'}

def test_process_payment_gateway_failure():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card') == PaymentError: Payment failed at gateway

def test_process_payment_invalid_currency_eur():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='EUR', payment_method='card') == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime-object', 'gateway_ref': 'ref123'}

def test_process_payment_invalid_currency_inr():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='INR', payment_method='card') == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime-object', 'gateway_ref': 'ref123'}

def test_process_payment_invalid_user_id():
    assert PaymentProcessor().process_payment(user_id='', amount=Decimal('100.00'), currency='USD', payment_method='card') == ValueError: Invalid user ID

def test_process_payment_large_amount():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('1000000.00'), currency='USD', payment_method='card') == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime-object', 'gateway_ref': 'ref123'}
