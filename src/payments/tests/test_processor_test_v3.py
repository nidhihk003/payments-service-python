def test_process_payment_successful_card_payment():
    assert PaymentProcessor().process_payment('user123', Decimal('100.00'), 'USD', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<gateway_reference>'}

def test_process_payment_successful_wallet_payment():
    assert PaymentProcessor().process_payment('user456', Decimal('50.00'), 'EUR', 'wallet') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<gateway_reference>'}

def test_process_payment_invalid_currency():
    assert PaymentProcessor().process_payment('user789', Decimal('20.00'), 'GBP', 'card') == {'exception': {'name': 'ValueError', 'message': 'Unsupported currency'}}

def test_process_payment_negative_amount():
    assert PaymentProcessor().process_payment('user321', Decimal('-10.00'), 'USD', 'card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_zero_amount():
    assert PaymentProcessor().process_payment('user654', Decimal('0.00'), 'USD', 'card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_gateway_failure():
    assert PaymentProcessor().process_payment('user987', Decimal('100.00'), 'USD', 'card') == {'exception': {'name': 'PaymentError', 'message': 'Payment failed at gateway'}}

def test_process_payment_high_amount():
    assert PaymentProcessor().process_payment('user111', Decimal('1000000.00'), 'USD', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<gateway_reference>'}

def test_process_payment_minimum_positive_amount():
    assert PaymentProcessor().process_payment('user222', Decimal('0.01'), 'USD', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<gateway_reference>'}

def test_process_payment_unsupported_payment_method():
    assert PaymentProcessor().process_payment('user333', Decimal('100.00'), 'USD', 'crypto') == {'exception': {'name': 'ValueError', 'message': 'Unsupported payment method'}}

def test_process_payment_large_decimal_amount():
    assert PaymentProcessor().process_payment('user444', Decimal('9999999999.99'), 'USD', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<gateway_reference>'}
