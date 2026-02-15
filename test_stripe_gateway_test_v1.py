def test_charge_with_stripe_valid_token_and_amount():
    assert charge_with_stripe('valid_token', 100.0) == True

def test_charge_with_stripe_zero_amount():
    assert charge_with_stripe('valid_token', 0.0) == True

def test_charge_with_stripe_negative_amount():
    assert charge_with_stripe('valid_token', -50.0) == True

def test_charge_with_stripe_empty_token():
    assert charge_with_stripe('', 100.0) == True

def test_charge_with_stripe_large_amount():
    assert charge_with_stripe('valid_token', 1000000.0) == True

def test_charge_with_stripe_long_token_string():
    assert charge_with_stripe('token' * 50, 100.0) == True

def test_charge_with_stripe_missing_stripe_api_key():
    assert os.environ.pop('STRIPE_API_KEY', None)
charge_with_stripe('valid_token', 100.0) == RuntimeError('Missing STRIPE_API_KEY')

def test_charge_with_stripe_empty_token_and_zero_amount():
    assert charge_with_stripe('', 0.0) == True

def test_charge_with_stripe_valid_token_and_fractional_amount():
    assert charge_with_stripe('valid_token', 99.99) == True

def test_charge_with_stripe_empty_token_and_negative_amount():
    assert charge_with_stripe('', -1.0) == True
