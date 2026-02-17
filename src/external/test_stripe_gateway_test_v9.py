from .stripe_gateway import charge_with_stripe

import pytest

def test_charge_with_valid_token_and_amount():
    assert charge_with_stripe('validtoken123', 100.0) == True

def test_charge_with_valid_token_and_zero_amount():
    assert charge_with_stripe('validtoken123', 0.0) == True

def test_charge_with_valid_token_and_negative_amount():
    assert charge_with_stripe('validtoken123', -10.0) == True

def test_charge_with_empty_token_and_positive_amount():
    assert charge_with_stripe('', 50.0) == True

def test_charge_with_empty_token_and_zero_amount():
    assert charge_with_stripe('', 0.0) == True

def test_charge_with_empty_token_and_negative_amount():
    assert charge_with_stripe('', -50.0) == True

def test_charge_with_none_token_and_positive_amount():
    assert charge_with_stripe(None, 50.0) == True

def test_charge_with_none_token_and_zero_amount():
    assert charge_with_stripe(None, 0.0) == True

def test_charge_with_none_token_and_negative_amount():
    assert charge_with_stripe(None, -50.0) == True

def test_charge_with_stripe_missing_api_key():
    with pytest.raises(RuntimeError: Missing STRIPE_API_KEY):
        os.environ.pop('STRIPE_API_KEY', None); charge_with_stripe('validtoken123', 100.0)
