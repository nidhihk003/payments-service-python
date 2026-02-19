from .processor import processor

import pytest

def test_process_payment_null_amount(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', None)

def test_process_payment_null_user_id(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment(None, Decimal('100.00'))

def test_process_payment_empty_currency(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), currency='')

def test_process_payment_invalid_currency(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), currency='ABC')

def test_process_payment_invalid_payment_method(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), payment_method='invalid_method')

def test_process_payment_large_currency_boundary_condition(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    processor._call_payment_gateway = lambda payload: {'status': 'success', 'reference': 'abc123'}
    assert processor.process_payment('user123', Decimal('1000000000000000.00')) == {'transaction_id': 'txn-<current_time>-<random_number>', 'status': 'SUCCESS', 'processed_at': '<current_datetime>', 'gateway_ref': 'abc123'}

def test_process_payment_minimum_positive_amount(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    processor._call_payment_gateway = lambda payload: {'status': 'success', 'reference': 'abc123'}
    assert processor.process_payment('user123', Decimal('0.01')) == {'transaction_id': 'txn-<current_time>-<random_number>', 'status': 'SUCCESS', 'processed_at': '<current_datetime>', 'gateway_ref': 'abc123'}

def test_process_payment_large_amount_edge_case(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
    processor = PaymentProcessor()
    processor._call_payment_gateway = lambda payload: {'status': 'success', 'reference': 'abc123'}
    assert processor.process_payment('user123', Decimal('9999999999999999.99')) == {'transaction_id': 'txn-<current_time>-<random_number>', 'status': 'SUCCESS', 'processed_at': '<current_datetime>', 'gateway_ref': 'abc123'}

def test_process_payment_invalid_string_amount(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', '100.00')

def test_process_payment_invalid_boolean_amount(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'test-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', True)
