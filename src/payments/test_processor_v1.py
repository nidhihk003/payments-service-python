def test_process_payment_valid_card_payment():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card') == {'transaction_id': 'txn-...', 'status': 'SUCCESS', 'processed_at': '...', 'gateway_ref': '...'}

def test_process_payment_valid_wallet_payment():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('150.00'), currency='USD', payment_method='wallet') == {'transaction_id': 'txn-...', 'status': 'SUCCESS', 'processed_at': '...', 'gateway_ref': '...'}

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('-10.00'), currency='USD', payment_method='card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_zero_amount():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('0.00'), currency='USD', payment_method='card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_unsupported_currency():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='GBP', payment_method='card') == {'exception': {'name': 'ValueError', 'message': 'Unsupported currency'}}

def test_process_payment_high_amount():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('1000000.00'), currency='USD', payment_method='card') == {'transaction_id': 'txn-...', 'status': 'SUCCESS', 'processed_at': '...', 'gateway_ref': '...'}

def test_process_payment_minimum_edge_amount():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('0.01'), currency='USD', payment_method='card') == {'transaction_id': 'txn-...', 'status': 'SUCCESS', 'processed_at': '...', 'gateway_ref': '...'}

def test_process_payment_valid_eur_payment():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('50.00'), currency='EUR', payment_method='card') == {'transaction_id': 'txn-...', 'status': 'SUCCESS', 'processed_at': '...', 'gateway_ref': '...'}

def test_process_payment_valid_inr_payment():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('5000.00'), currency='INR', payment_method='card') == {'transaction_id': 'txn-...', 'status': 'SUCCESS', 'processed_at': '...', 'gateway_ref': '...'}

def test_process_payment_gateway_failure():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card') == {'exception': {'name': 'PaymentError', 'message': 'Payment failed at gateway'}}
