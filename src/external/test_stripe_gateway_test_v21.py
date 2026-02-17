from .stripe_gateway import charge_with_stripe

import pytest

def test_successful_charge_with_valid_token_and_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', 100.0) == True

def test_successful_charge_with_token_and_zero_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', 0.0) == True

def test_successful_charge_with_token_and_negative_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', -50.0) == True

def test_missing_stripe_api_key_raises_runtime_error(monkeypatch):
    with pytest.raises(RuntimeError):
        monkeypatch.delenv('STRIPE_API_KEY', raising=False)
        charge_with_stripe('valid_token', 100.0)

def test_missing_stripe_api_key_with_zero_amount_raises_runtime_error(monkeypatch):
    with pytest.raises(RuntimeError):
        monkeypatch.delenv('STRIPE_API_KEY', raising=False)
        charge_with_stripe('valid_token', 0.0)

def test_missing_stripe_api_key_with_negative_amount_raises_runtime_error(monkeypatch):
    with pytest.raises(RuntimeError):
        monkeypatch.delenv('STRIPE_API_KEY', raising=False)
        charge_with_stripe('valid_token', -50.0)

def test_successful_charge_with_different_token_format(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('12345', 100.0) == True

def test_successful_charge_with_large_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', 1000000.0) == True

def test_successful_charge_with_small_amount(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('valid_token', 0.01) == True

def test_successful_charge_with_long_token(monkeypatch):
    monkeypatch.setenv('STRIPE_API_KEY', 'dummy_key')
    assert charge_with_stripe('a'*256, 100.0) == True
