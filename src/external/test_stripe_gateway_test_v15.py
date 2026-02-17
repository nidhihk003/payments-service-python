from .stripe_gateway import charge_with_stripe

import pytest

def test_charge_with_valid_token_and_amount():
    assert charge_with_stripe('valid_token', 100.0) == True

def test_charge_with_valid_token_and_zero_amount():
    assert charge_with_stripe('valid_token', 0.0) == True

def test_charge_with_valid_token_and_negative_amount():
    assert charge_with_stripe('valid_token', -50.0) == True

def test_charge_with_empty_token_and_positive_amount():
    assert charge_with_stripe('', 50.0) == True

def test_charge_with_whitespace_token_and_positive_amount():
    assert charge_with_stripe(' ', 50.0) == True

def test_charge_with_long_token_and_positive_amount():
    assert charge_with_stripe('a' * 1000, 50.0) == True

def test_charge_with_valid_token_and_large_amount():
    assert charge_with_stripe('valid_token', 1e6) == True

def test_charge_with_missing_api_key():
    with pytest.raises(RuntimeError):
        charge_with_stripe('valid_token', 100.0)

def test_charge_with_valid_token_and_nan_amount():
    assert charge_with_stripe('valid_token', float('nan')) == True

def test_charge_with_valid_token_and_infinity_amount():
    assert charge_with_stripe('valid_token', float('inf')) == True
