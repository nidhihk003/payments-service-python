from .processor import processor

import pytest

def test_process_payment_success(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
    monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
    monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'success', 'reference': 'ref123'})
    result = processor.process_payment('user123', Decimal('100.00'))
    result['processed_at'] = datetime.datetime(2023, 10, 1, 0, 0, 0)
    assert result == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime(2023, 10, 1, 0, 0, 0)', 'gateway_ref': 'ref123'}

def test_process_payment_zero_amount(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('0.00'))

def test_process_payment_negative_amount(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('-10.00'))

def test_process_payment_unsupported_currency(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), 'JPY')

def test_process_payment_gateway_failure(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
        monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
        monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'failure'})
        processor.process_payment('user123', Decimal('100.00'))

def test_process_payment_with_eur_currency(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'EUR', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
    monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
    monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'success', 'reference': 'ref123'})
    result = processor.process_payment('user123', Decimal('100.00'), 'EUR')
    result['processed_at'] = datetime.datetime(2023, 10, 1, 0, 0, 0)
    assert result == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime(2023, 10, 1, 0, 0, 0)', 'gateway_ref': 'ref123'}

def test_process_payment_with_inr_currency(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'INR', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
    monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
    monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'success', 'reference': 'ref123'})
    result = processor.process_payment('user123', Decimal('100.00'), 'INR')
    result['processed_at'] = datetime.datetime(2023, 10, 1, 0, 0, 0)
    assert result == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime(2023, 10, 1, 0, 0, 0)', 'gateway_ref': 'ref123'}

def test_process_payment_with_wallet_method(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'USD', 'method': 'wallet', 'timestamp': '2023-10-01T00:00:00'}
    monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
    monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'success', 'reference': 'ref123'})
    result = processor.process_payment('user123', Decimal('100.00'), 'USD', 'wallet')
    result['processed_at'] = datetime.datetime(2023, 10, 1, 0, 0, 0)
    assert result == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime(2023, 10, 1, 0, 0, 0)', 'gateway_ref': 'ref123'}

def test_process_payment_missing_environment_variables(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.delenv('PAYMENT_GATEWAY_URL', raising=False)
        monkeypatch.delenv('PAYMENT_API_KEY', raising=False)
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), 'USD', 'wallet')

def test_process_payment_invalid_gateway_response(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
        monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
        monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'unknown_status'})
        processor.process_payment('user123', Decimal('100.00'))

def test_process_payment_empty_user_id(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('', Decimal('100.00'))

def test_process_payment_invalid_payment_method(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), 'USD', 'unsupported_method')

def test_process_payment_large_amount(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '1000000.00', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
    monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
    monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'success', 'reference': 'ref123'})
    result = processor.process_payment('user123', Decimal('1000000.00'))
    result['processed_at'] = datetime.datetime(2023, 10, 1, 0, 0, 0)
    assert result == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime(2023, 10, 1, 0, 0, 0)', 'gateway_ref': 'ref123'}

def test_process_payment_small_amount(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '0.01', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
    monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
    monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'success', 'reference': 'ref123'})
    result = processor.process_payment('user123', Decimal('0.01'))
    result['processed_at'] = datetime.datetime(2023, 10, 1, 0, 0, 0)
    assert result == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime(2023, 10, 1, 0, 0, 0)', 'gateway_ref': 'ref123'}

def test_process_payment_boundary_above_zero(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '0.01', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
    monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
    monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {'status': 'success', 'reference': 'ref123'})
    result = processor.process_payment('user123', Decimal('0.01'))
    result['processed_at'] = datetime.datetime(2023, 10, 1, 0, 0, 0)
    assert result == {'transaction_id': 'txn-1234567890-1234', 'status': 'SUCCESS', 'processed_at': 'datetime.datetime(2023, 10, 1, 0, 0, 0)', 'gateway_ref': 'ref123'}

def test_process_payment_boundary_below_zero(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('-0.01'))

def test_process_payment_gateway_http_error(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
        monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
        monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: raise PaymentError('Gateway error'))
        processor.process_payment('user123', Decimal('100.00'))

def test_process_payment_gateway_invalid_response_structure(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        payload = {'transaction_id': 'txn-1234567890-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-01T00:00:00'}
        monkeypatch.setattr(processor, '_generate_transaction_id', lambda: 'txn-1234567890-1234')
        monkeypatch.setattr(PaymentProcessor, '_call_payment_gateway', lambda self, payload: {})
        processor.process_payment('user123', Decimal('100.00'))
