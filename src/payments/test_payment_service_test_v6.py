from .payment_service import payment_service

import pytest

def test_calculate_payment_fee_null_amount():
    with pytest.raises(TypeError):
        calculate_payment_fee(None)

def test_calculate_payment_fee_string_amount():
    with pytest.raises(TypeError):
        calculate_payment_fee('100.0')

def test_calculate_payment_fee_empty_amount():
    with pytest.raises(TypeError):
        calculate_payment_fee()

def test_apply_discount_null_amount():
    with pytest.raises(TypeError):
        apply_discount(None, 10.0)

def test_apply_discount_null_percentage():
    with pytest.raises(TypeError):
        apply_discount(200.0, None)

def test_apply_discount_string_amount():
    with pytest.raises(TypeError):
        apply_discount('200.0', 10.0)

def test_process_payment_null_user_id():
    assert PaymentProcessor().process_payment(None, Decimal('100.0'), 'USD', 'card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_null_amount():
    with pytest.raises(AttributeError):
        PaymentProcessor().process_payment('user123', None, 'USD', 'card')

def test_process_payment_null_currency():
    assert PaymentProcessor().process_payment('user123', Decimal('100.0'), None, 'card') == {'exception': {'name': 'ValueError', 'message': 'Unsupported currency'}}

def test_process_payment_null_payment_method():
    assert PaymentProcessor().process_payment('user123', Decimal('100.0'), 'USD', None) == {'exception': {'name': 'PaymentError', 'message': 'Payment failed at gateway'}}
