from .payment_service import unknown_function

import pytest

def test_calculate_payment_fee_standard_amount():
    assert calculate_payment_fee(100.0) == 103.0

def test_calculate_payment_fee_zero_amount():
    assert calculate_payment_fee(0.0) == 0.0

def test_calculate_payment_fee_negative_amount():
    assert calculate_payment_fee(-50.0) == -51.5

def test_calculate_payment_fee_large_amount():
    assert calculate_payment_fee(1e6) == 1030000.0

def test_apply_discount_standard_case():
    assert apply_discount(200.0, 10.0) == 180.0

def test_apply_discount_no_discount():
    assert apply_discount(200.0, 0.0) == 200.0

def test_apply_discount_full_discount():
    assert apply_discount(200.0, 100.0) == 0.0

def test_apply_discount_invalid_negative_discount():
    with pytest.raises(ValueError):
        apply_discount(200.0, -10.0)

def test_apply_discount_invalid_over_100_discount():
    with pytest.raises(ValueError):
        apply_discount(200.0, 110.0)

def test_process_payment_successful():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('100.0'), 'USD', 'card') == {'transaction_id': 'some-uuid', 'status': 'SUCCESS', 'processed_at': 'some-timestamp', 'gateway_ref': 'some-gateway-ref'}

def test_process_payment_negative_amount():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('-100.0'), 'USD', 'card') == {'exception': {'name': 'ValueError', 'message': 'Amount must be positive'}}

def test_process_payment_unsupported_currency():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('100.0'), 'GBP', 'card') == {'exception': {'name': 'ValueError', 'message': 'Unsupported currency'}}

def test_process_payment_unsupported_payment_method():
    processor = PaymentProcessor()
    assert processor.process_payment('user123', Decimal('100.0'), 'USD', 'bank_transfer') == {'exception': {'name': 'PaymentError', 'message': 'Payment failed at gateway'}}
