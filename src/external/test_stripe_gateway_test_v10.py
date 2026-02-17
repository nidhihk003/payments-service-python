from .stripe_gateway import charge_with_stripe

import pytest

def test_charge_with_stripe_valid_token_amount():
    assert charge_with_stripe('valid_token', 100.0) == True

def test_charge_with_stripe_missing_api_key():
    with pytest.raises(raises):
        charge_with_stripe('valid_token', 100.0)

def test_charge_with_stripe_zero_amount():
    assert charge_with_stripe('valid_token', 0.0) == True

def test_charge_with_stripe_negative_amount():
    assert charge_with_stripe('valid_token', -50.0) == True

def test_charge_with_stripe_empty_token():
    assert charge_with_stripe('', 100.0) == True

def test_charge_with_stripe_large_amount():
    assert charge_with_stripe('valid_token', 1000000.0) == True

def test_charge_with_stripe_special_characters_in_token():
    assert charge_with_stripe('tok@en#123$', 100.0) == True

def test_charge_with_stripe_non_string_token():
    with pytest.raises(raises):
        charge_with_stripe(12345, 100.0)

def test_charge_with_stripe_non_float_amount():
    with pytest.raises(raises):
        charge_with_stripe('valid_token', '100.0')

def test_charge_with_stripe_none_token():
    with pytest.raises(raises):
        charge_with_stripe(None, 100.0)
