def test_process_payment_valid_card_usd():
    assert PaymentProcessor().process_payment('user-123', Decimal('100.00'), 'USD', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_zero_amount():
    assert PaymentProcessor().process_payment('user-123', Decimal('0.00'), 'USD', 'card') == ValueError('Amount must be positive')

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment('user-123', Decimal('-1.00'), 'USD', 'card') == ValueError('Amount must be positive')

def test_process_payment_unsupported_currency():
    assert PaymentProcessor().process_payment('user-123', Decimal('100.00'), 'GBP', 'card') == ValueError('Unsupported currency')

def test_process_payment_valid_eur_wallet():
    assert PaymentProcessor().process_payment('user-123', Decimal('50.00'), 'EUR', 'wallet') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_gateway_error():
    assert PaymentProcessor().process_payment('user-123', Decimal('100.00'), 'USD', 'card') == PaymentError('Payment failed at gateway')

def test_process_payment_valid_inr_card():
    assert PaymentProcessor().process_payment('user-123', Decimal('1000.00'), 'INR', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_generate_transaction_id_format():
    assert PaymentProcessor()._generate_transaction_id() == txn-<timestamp>-<random>

def test_call_payment_gateway_success():
    assert PaymentProcessor()._call_payment_gateway({'user_id': 'user-123', 'amount': '100.00', 'currency': 'USD', 'method': 'card'}) == {'status': 'success', 'reference': '<reference>'}

def test_call_payment_gateway_error_status_code():
    assert PaymentProcessor()._call_payment_gateway({'user_id': 'user-123', 'amount': '100.00', 'currency': 'USD', 'method': 'card'}) == PaymentError('Gateway error: <response_text>')
