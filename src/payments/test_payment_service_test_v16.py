from .payment_service import payment_service

import pytest

def test_calculate_payment_fee_none_amount():
    with pytest.raises(TypeError):
        calculate_payment_fee(None)

def test_apply_discount_none_amount():
    with pytest.raises(TypeError):
        apply_discount(None, 20.0)

def test_apply_discount_none_percentage():
    with pytest.raises(TypeError):
        apply_discount(100.0, None)

def test_apply_discount_amount_as_none_and_percentage_as_none():
    with pytest.raises(TypeError):
        apply_discount(None, None)

def test_process_payment_none_user_id():
    processor = PaymentProcessor()
    assert processor.process_payment(None, Decimal('100.0'), 'USD', 'card') == {'transaction_id': 'txn-xxxxxxxx', 'status': 'SUCCESS', 'processed_at': 'yyyy-mm-ddThh:mm:ss.zzzzzz', 'gateway_ref': 'gw-xxxxxx'}

def test_process_payment_none_amount():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user123', None, 'USD', 'card')

def test_process_payment_none_currency():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.0'), None, 'card')

def test_process_payment_none_payment_method():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user123', Decimal('100.0'), 'USD', None)

def test_process_payment_all_none():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment(None, None, None, None)

def test_process_payment_invalid_amount_type():
    with pytest.raises(TypeError):
        processor = PaymentProcessor()
        processor.process_payment('user123', '100.0', 'USD', 'card')
