from .stripe_gateway import charge_with_stripe

import pytest

def test_successful_charge_with_valid_stripe_api_key(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'valid_key')
    assert charge_with_stripe('dummy_token', 100.0) == True

def test_missing_stripe_api_key_raises_runtime_error(monkeypatch):
    with pytest.raises(RuntimeError):
        monkeypatch.delenv('STRIPE_API_KEY', raising=False)
        charge_with_stripe('dummy_token', 100.0)

def test_charge_with_minimum_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'valid_key')
    assert charge_with_stripe('dummy_token', 0.01) == True

def test_charge_with_large_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'valid_key')
    assert charge_with_stripe('dummy_token', 1000000.0) == True

def test_charge_with_zero_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'valid_key')
    assert charge_with_stripe('dummy_token', 0.0) == True
