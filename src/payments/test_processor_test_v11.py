from .processor import processor

import pytest

def test_process_payment_with_null_user_id(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment(None, Decimal('100.00'), 'USD', 'card')

def test_process_payment_with_empty_user_id(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('', Decimal('100.00'), 'USD', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_with_float_amount(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('99.99'), 'USD', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_with_non_decimal_amount(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', 100.00, 'USD', 'card')

def test_process_payment_with_minimal_supported_currency_inr(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('0.01'), 'INR', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_with_invalid_payment_method(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('100.00'), 'USD', 'crypto') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_with_null_amount(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', None, 'USD', 'card')

def test_process_payment_with_missing_currency(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), None, 'card')

def test_process_payment_with_large_string_amount(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('1e+1000'), 'USD', 'card')

def test_process_payment_with_nonexistent_environment_variable(monkeypatch):
    with pytest.raises(PaymentError):
        monkeypatch.delenv('PAYMENT_GATEWAY_URL', raising=False)
        monkeypatch.delenv('PAYMENT_API_KEY', raising=False)
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.00'), 'USD', 'card')
