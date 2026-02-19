from .payment_service import payment_service

import pytest

def test_calculate_payment_fee_with_null():
    with pytest.raises(TypeError):
        calculate_payment_fee(None)

def test_calculate_payment_fee_with_string():
    with pytest.raises(TypeError):
        calculate_payment_fee('100.0')

def test_calculate_payment_fee_with_empty_input():
    with pytest.raises(TypeError):
        calculate_payment_fee()

def test_apply_discount_with_null_amount():
    with pytest.raises(TypeError):
        apply_discount(None, 20.0)

def test_apply_discount_with_null_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, None)

def test_apply_discount_with_string_amount():
    with pytest.raises(TypeError):
        apply_discount('100.0', 20.0)

def test_apply_discount_with_string_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, '20.0')

def test_apply_discount_with_empty_inputs():
    with pytest.raises(TypeError):
        apply_discount()

def test_process_payment_with_null_user_id():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment(None, Decimal('100.0'), 'USD', 'card')

def test_process_payment_with_null_amount():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user_123', None, 'USD', 'card')
