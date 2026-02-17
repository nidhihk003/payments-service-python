from .stripe_gateway import charge_with_stripe

import pytest

def test_successful_stripe_charge():
    assert charge_with_stripe('valid_token', 100.0) == True

def test_missing_stripe_api_key(monkeypatch):
    with pytest.raises(raises RuntimeError):
        monkeypatch.delenv('STRIPE_API_KEY', raising=False); charge_with_stripe('valid_token', 100.0)

def test_zero_amount_charge():
    assert charge_with_stripe('valid_token', 0.0) == True

def test_negative_amount_charge():
    assert charge_with_stripe('valid_token', -50.0) == True

def test_large_amount_charge():
    assert charge_with_stripe('valid_token', 1000000.0) == True

def test_empty_token():
    assert charge_with_stripe('', 100.0) == True

def test_special_characters_in_token():
    assert charge_with_stripe('!@#$%^&*', 100.0) == True

def test_non_numeric_amount():
    assert charge_with_stripe('valid_token', 'not_a_number') == True

def test_missing_amount():
    with pytest.raises(raises TypeError):
        charge_with_stripe('valid_token')

def test_missing_token():
    with pytest.raises(raises TypeError):
        charge_with_stripe(100.0)
