from .src.payments.processor import processor

import pytest

def test_process_payment_minimum_positive_amount_usd_wallet(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('user201', Decimal('0.01'), 'USD', 'wallet') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_invalid_currency_symbol(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user202', Decimal('100.00'), '$USD', 'card')

def test_process_payment_boundary_currency_symbol(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user203', Decimal('100.00'), 'USD$', 'card')

def test_process_payment_empty_amount(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user204', Decimal(''), 'USD', 'card')

def test_process_payment_large_negative_amount(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user205', Decimal('-999999999.99'), 'USD', 'card')

def test_process_payment_invalid_amount_type(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user206', '100.00', 'USD', 'card')

def test_process_payment_large_amount_eur_wallet(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('user207', Decimal('999999999.99'), 'EUR', 'wallet') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_large_amount_inr_card(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('user208', Decimal('999999999.99'), 'INR', 'card') == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}

def test_process_payment_null_currency(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
        monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
        processor = PaymentProcessor()
        processor.process_payment('user209', Decimal('100.00'), None, 'card')

def test_process_payment_null_payment_method(monkeypatch):
    monkeypatch.setenv('PAYMENT_GATEWAY_URL', 'https://api.fakepay.com/charge')
    monkeypatch.setenv('PAYMENT_API_KEY', 'hardcoded-key')
    processor = PaymentProcessor()
    assert processor.process_payment('user210', Decimal('100.00'), 'USD', None) == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': '<reference>'}
