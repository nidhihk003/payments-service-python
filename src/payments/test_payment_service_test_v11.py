from .payment_service import payment_service

import pytest

def test_calculate_payment_fee_with_null_input():
    with pytest.raises(TypeError):
        calculate_payment_fee(None)

def test_calculate_payment_fee_with_string_input():
    with pytest.raises(TypeError):
        calculate_payment_fee('100.0')

def test_apply_discount_with_null_amount():
    with pytest.raises(TypeError):
        apply_discount(None, 10.0)

def test_apply_discount_with_null_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, None)

def test_apply_discount_with_string_amount():
    with pytest.raises(TypeError):
        apply_discount('100.0', 10.0)

def test_apply_discount_with_string_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, '10.0')

def test_process_payment_with_null_user_id():
    assert PaymentProcessor().process_payment(None, Decimal('100.0'), 'USD', 'card') == {'transaction_id': 'txn-xxxxxxxx', 'status': 'SUCCESS', 'processed_at': 'yyyy-mm-ddThh:mm:ss.ssssss', 'gateway_ref': 'gw-xxxxxx'}

def test_process_payment_with_null_amount():
    with pytest.raises(TypeError):
        PaymentProcessor().process_payment('user123', None, 'USD', 'card')

def test_process_payment_with_null_currency():
    with pytest.raises(TypeError):
        PaymentProcessor().process_payment('user123', Decimal('100.0'), None, 'card')

def test_process_payment_with_null_payment_method():
    with pytest.raises(TypeError):
        PaymentProcessor().process_payment('user123', Decimal('100.0'), 'USD', None)
