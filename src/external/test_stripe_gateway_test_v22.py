from .stripe_gateway import charge_with_stripe

import pytest

def test_charge_with_valid_token_and_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', 100.0) == True

def test_charge_with_valid_token_and_zero_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', 0.0) == True

def test_charge_with_valid_token_and_negative_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', -50.0) == True

def test_charge_with_empty_token(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('', 100.0) == True

def test_charge_with_empty_token_and_zero_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('', 0.0) == True

def test_charge_with_empty_token_and_negative_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('', -50.0) == True

def test_charge_with_missing_api_key(monkeypatch):
    with pytest.raises(RuntimeError):
        monkeypatch.delenv('STRIPE_API_KEY', raising=False)
        charge_with_stripe('valid_token', 100.0)

def test_charge_with_none_api_key(monkeypatch):
    with pytest.raises(RuntimeError):
        monkeypatch.setenv('STRIPE_API_KEY', '')
        charge_with_stripe('valid_token', 100.0)

def test_charge_with_special_characters_in_token(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('!@#$%^&*()', 100.0) == True

def test_charge_with_large_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', 1e6) == True
