from .src.payments.payment_service import payment_service

import pytest

def test_calculate_payment_fee_null_amount():
    with pytest.raises(TypeError):
        calculate_payment_fee(None)

def test_calculate_payment_fee_string_amount():
    with pytest.raises(TypeError):
        calculate_payment_fee('100.0')

def test_apply_discount_null_amount():
    with pytest.raises(TypeError):
        apply_discount(None, 10.0)

def test_apply_discount_null_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, None)

def test_apply_discount_string_amount():
    with pytest.raises(TypeError):
        apply_discount('100.0', 10.0)

def test_apply_discount_string_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, '10.0')

def test_process_payment_invalid_amount_type():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user123', '100.0', 'USD', 'card')

def test_process_payment_null_currency():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.0'), None, 'card')

def test_process_payment_null_payment_method():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.0'), 'USD', None)

def test_process_payment_empty_user_id():
    processor = PaymentProcessor()
    assert processor.process_payment('', Decimal('100.0'), 'USD', 'card') == {'transaction_id': 'txn-xxxxxxxx', 'status': 'SUCCESS', 'processed_at': 'xxxx-xx-xxTxx:xx:xx.xxxxxx', 'gateway_ref': 'gw-xxxxxx'}
