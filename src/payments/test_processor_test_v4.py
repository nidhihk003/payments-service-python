def test_process_payment_valid_card_usd():
    assert PaymentProcessor().process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_valid_wallet_eur():
    assert PaymentProcessor().process_payment(user_id='user456', amount=Decimal('50.00'), currency='EUR', payment_method='wallet') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_invalid_currency():
    assert PaymentProcessor().process_payment(user_id='user789', amount=Decimal('30.00'), currency='GBP', payment_method='card') == ValueError('Unsupported currency')

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment(user_id='user101', amount=Decimal('-10.00'), currency='USD', payment_method='card') == ValueError('Amount must be positive')

def test_process_payment_zero_amount():
    assert PaymentProcessor().process_payment(user_id='user102', amount=Decimal('0.00'), currency='USD', payment_method='card') == ValueError('Amount must be positive')

def test_process_payment_gateway_error():
    assert PaymentProcessor().process_payment(user_id='user103', amount=Decimal('20.00'), currency='USD', payment_method='card') == PaymentError('Gateway error: <error_message>')

def test_process_payment_gateway_failure():
    assert PaymentProcessor().process_payment(user_id='user104', amount=Decimal('75.00'), currency='INR', payment_method='wallet') == PaymentError('Payment failed at gateway')

def test_generate_transaction_id_format():
    assert PaymentProcessor()._generate_transaction_id() == txn-<timestamp>-<random>

def test_call_payment_gateway_successful_response():
    assert PaymentProcessor()._call_payment_gateway(payload={'amount': '30.00', 'currency': 'USD'}) == {'status': 'success', 'reference': '<reference>'}

def test_call_payment_gateway_error_response():
    assert PaymentProcessor()._call_payment_gateway(payload={'amount': '30.00', 'currency': 'USD'}) == PaymentError('Gateway error: <error_message>')
