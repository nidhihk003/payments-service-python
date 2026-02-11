import pytest
from decimal import Decimal

from payments.processor import PaymentProcessor, PaymentError


def test_negative_amount_fails():
    processor = PaymentProcessor()

    with pytest.raises(ValueError):
        processor.process_payment(
            user_id="user-123",
            amount=Decimal("-10.00"),
            currency="USD",
        )


def test_unsupported_currency_fails():
    processor = PaymentProcessor()

    with pytest.raises(ValueError):
        processor.process_payment(
            user_id="user-123",
            amount=Decimal("100.00"),
            currency="JPY",  # ❌ unsupported
        )


def test_successful_payment_returns_success_status():
    """
    ❌ THIS TEST WILL FAIL
    Reason:
    - Makes real HTTP call
    - No mocking
    - Gateway URL is fake
    """
    processor = PaymentProcessor()

    result = processor.process_payment(
        user_id="user-456",
        amount=Decimal("50.00"),
        currency="USD",
    )

    # ❌ This assertion will never be reached
    assert result["status"] == "SUCCESS"


def test_transaction_id_is_not_none():
    """
    ❌ Flaky test:
    - Relies on time/random
    """
    processor = PaymentProcessor()

    txn_id = processor._generate_transaction_id()

    assert txn_id is not None
    assert txn_id.startswith("txn-")
