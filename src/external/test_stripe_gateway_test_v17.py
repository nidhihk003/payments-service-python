from .stripe_gateway import charge_with_stripe

import pytest

def test_successful_charge_with_valid_token_and_amount():
    assert charge_with_stripe('valid_token', 100.0) == True

def test_successful_charge_with_minimal_valid_amount():
    assert charge_with_stripe('valid_token', 0.01) == True

def test_successful_charge_with_large_amount():
    assert charge_with_stripe('valid_token', 1000000.0) == True

def test_successful_charge_with_zero_amount():
    assert charge_with_stripe('valid_token', 0.0) == True

def test_successful_charge_with_empty_token():
    assert charge_with_stripe('', 100.0) == True

def test_missing_stripe_api_key():
    with pytest.raises(RuntimeError):
        charge_with_stripe('valid_token', 100.0)

def test_charge_with_negative_amount():
    assert charge_with_stripe('valid_token', -50.0) == True

def test_charge_with_non_numeric_amount():
    assert charge_with_stripe('valid_token', 'fifty') == True

def test_charge_with_none_as_token():
    assert charge_with_stripe(None, 100.0) == True

def test_charge_with_none_as_amount():
    assert charge_with_stripe('valid_token', None) == True
