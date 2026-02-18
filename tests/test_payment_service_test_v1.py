from .src.payments.payment_service import unknown_function

import pytest

def test_calculate_payment_fee_positive_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-50.0) == -51.5

def test_apply_discount_valid_discount():
    assert apply_discount(200.0, 20.0) == 160.0

def test_apply_discount_zero_discount():
    assert apply_discount(200.0, 0.0) == 200.0

def test_apply_discount_full_discount():
    assert apply_discount(200.0, 100.0) == 0.0

def test_apply_discount_negative_discount():
    with pytest.raises(ValueError):
        apply_discount(200.0, -10.0)

def test_apply_discount_above_100_discount():
    with pytest.raises(ValueError):
        apply_discount(200.0, 110.0)

def test_process_payment_successful():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('100.00'), 'USD', 'card') == {'transaction_id': 'txn-xxxxxxxx', 'status': 'SUCCESS', 'processed_at': 'xxxx-xx-xxTxx:xx:xx.xxxxxx', 'gateway_ref': 'gw-xxxxxx'}

def test_process_payment_zero_amount():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('0.00'), 'USD', 'card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_unsupported_currency():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('100.00'), 'GBP', 'card') == {'exception': {'name': 'ValueError', 'message': 'Unsupported currency'}}

def test_process_payment_unsupported_method():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('100.00'), 'USD', 'bank_transfer') == {'exception': {'name': 'PaymentError', 'message': 'Payment failed at gateway'}}
