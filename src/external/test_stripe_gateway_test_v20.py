from .stripe_gateway import charge_with_stripe

import pytest

def test_charge_with_stripe_successful_charge():
    import os
    from src.external.stripe_gateway import charge_with_stripe
    os.environ['STRIPE_API_KEY'] = 'dummy_key'
    assert charge_with_stripe('test_token', 100.0) == True

def test_charge_with_stripe_missing_api_key():
    with pytest.raises(RuntimeError):
        import os
        from src.external.stripe_gateway import charge_with_stripe
        os.environ.pop('STRIPE_API_KEY', None)
        charge_with_stripe('test_token', 100.0)

def test_charge_with_stripe_zero_amount():
    import os
    from src.external.stripe_gateway import charge_with_stripe
    os.environ['STRIPE_API_KEY'] = 'dummy_key'
    assert charge_with_stripe('test_token', 0.0) == True

def test_charge_with_stripe_negative_amount():
    import os
    from src.external.stripe_gateway import charge_with_stripe
    os.environ['STRIPE_API_KEY'] = 'dummy_key'
    assert charge_with_stripe('test_token', -50.0) == True

def test_charge_with_stripe_large_amount():
    import os
    from src.external.stripe_gateway import charge_with_stripe
    os.environ['STRIPE_API_KEY'] = 'dummy_key'
    assert charge_with_stripe('test_token', 1000000.0) == True

def test_charge_with_stripe_empty_token():
    import os
    from src.external.stripe_gateway import charge_with_stripe
    os.environ['STRIPE_API_KEY'] = 'dummy_key'
    assert charge_with_stripe('', 100.0) == True

def test_charge_with_stripe_empty_api_key():
    with pytest.raises(RuntimeError):
        import os
        from src.external.stripe_gateway import charge_with_stripe
        os.environ['STRIPE_API_KEY'] = ''
        charge_with_stripe('test_token', 100.0)

def test_charge_with_stripe_non_string_token():
    import os
    from src.external.stripe_gateway import charge_with_stripe
    os.environ['STRIPE_API_KEY'] = 'dummy_key'
    assert charge_with_stripe(12345, 100.0) == True

def test_charge_with_stripe_non_float_amount():
    import os
    from src.external.stripe_gateway import charge_with_stripe
    os.environ['STRIPE_API_KEY'] = 'dummy_key'
    assert charge_with_stripe('test_token', '100.0') == True

def test_charge_with_stripe_no_environment_setup():
    with pytest.raises(RuntimeError):
        from src.external.stripe_gateway import charge_with_stripe
        charge_with_stripe('test_token', 100.0)
