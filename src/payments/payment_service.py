from decimal import Decimal, InvalidOperation
from datetime import datetime
import uuid


# -----------------------------
# Payment fee calculation
# -----------------------------

def calculate_payment_fee(amount: float) -> float:
    """
    Adds a 3% fee to the amount.
    Works for positive, zero, negative, and extreme float values.
    """
    return amount * 1.03


# -----------------------------
# Discount calculation
# -----------------------------

def apply_discount(amount: float, percentage: float) -> float:
    """
    Apply percentage discount on amount.
    """
    if percentage < 0 or percentage > 100:
        raise ValueError("Invalid discount")

    return amount * (1 - (percentage / 100))


# -----------------------------
# Payment Processor
# -----------------------------

class PaymentError(Exception):
    pass


class PaymentProcessor:

    SUPPORTED_CURRENCIES = {"USD", "EUR", "INR"}
    SUPPORTED_METHODS = {"card", "wallet"}

    def process_payment(
        self,
        user_id: str,
        amount: Decimal,
        currency: str,
        payment_method: str
    ) -> dict:
        # ---- Validation ----
        if amount <= Decimal("0"):
            return {
                "exception": {
                    "name": "ValueError",
                    "message": "Amount must be positive"
                }
            }

        if currency not in self.SUPPORTED_CURRENCIES:
            return {
                "exception": {
                    "name": "ValueError",
                    "message": "Unsupported currency"
                }
            }

        if payment_method not in self.SUPPORTED_METHODS:
            return {
                "exception": {
                    "name": "PaymentError",
                    "message": "Payment failed at gateway"
                }
            }

        # ---- Simulate gateway success ----
        return {
            "transaction_id": f"txn-{uuid.uuid4().hex[:8]}",
            "status": "SUCCESS",
            "processed_at": datetime.utcnow().isoformat(),
            "gateway_ref": f"gw-{uuid.uuid4().hex[:6]}"
        }
