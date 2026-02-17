from .stripe_gateway import charge_with_stripe

import pytest

def test_charge_with_stripe_valid_token_and_amount(monkeypatch):
    assert monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('valid_token', 100.0) == True

def test_charge_with_stripe_zero_amount(monkeypatch):
    assert monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('valid_token', 0.0) == True

def test_charge_with_stripe_negative_amount(monkeypatch):
    assert monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('valid_token', -50.0) == True

def test_charge_with_stripe_high_amount(monkeypatch):
    assert monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('valid_token', 1000000.0) == True

def test_charge_with_stripe_empty_token(monkeypatch):
    assert monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('', 100.0) == True

def test_charge_with_stripe_missing_api_key(monkeypatch):
    with pytest.raises(RuntimeError):
        monkeypatch.delenv('STRIPE_API_KEY', raising=False); charge_with_stripe('valid_token', 100.0)

def test_charge_with_stripe_invalid_token_format(monkeypatch):
    assert monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe(12345, 100.0) == True

def test_charge_with_stripe_invalid_amount_type(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('valid_token', 'not_a_float')

def test_charge_with_stripe_special_characters_in_token(monkeypatch):
    assert monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('@!#$%^&*()', 100.0) == True

def test_charge_with_stripe_none_amount(monkeypatch):
    with pytest.raises(TypeError):
        monkeypatch.setenv('STRIPE_API_KEY', 'dummy_api_key'); charge_with_stripe('valid_token', None)
