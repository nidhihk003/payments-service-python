import os
import time
import uuid
import json
import random
import logging
import decimal
import datetime
import requests
from typing import Dict, Any, Optional
from decimal import Decimal

# ---- global config (hard to mock) ----
PAYMENT_GATEWAY_URL = os.getenv("PAYMENT_GATEWAY_URL", "https://api.fakepay.com/charge")
API_KEY = os.getenv("PAYMENT_API_KEY", "hardcoded-key")  # ❌ bad practice
TIMEOUT_SECONDS = 5

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PaymentError(Exception):
    pass


class PaymentProcessor:
    """
    Core payment processor for card and wallet payments.
    """

    def __init__(self):
        # ❌ Non-deterministic state
        self.instance_id = uuid.uuid4().hex
        self.started_at = datetime.datetime.utcnow()

    def _generate_transaction_id(self) -> str:
        # ❌ Random + time based
        return f"txn-{int(time.time())}-{random.randint(1000, 9999)}"

    def _call_payment_gateway(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        ❌ Untestable:
        - real HTTP call
        - hardcoded URL
        - hardcoded API key
        """
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            PAYMENT_GATEWAY_URL,
            headers=headers,
            json=payload,
            timeout=TIMEOUT_SECONDS,
        )

        if response.status_code != 200:
            raise PaymentError(f"Gateway error: {response.text}")

        return response.json()

    def process_payment(
        self,
        user_id: str,
        amount: Decimal,
        currency: str = "USD",
        payment_method: str = "card",
    ) -> Dict[str, Any]:
        """
        Main entrypoint for processing a payment.
        """

        if amount <= Decimal("0"):
            raise ValueError("Amount must be positive")

        if currency not in {"USD", "EUR", "INR"}:
            raise ValueError("Unsupported currency")

        txn_id = self._generate_transaction_id()

        payload = {
            "transaction_id": txn_id,
            "user_id": user_id,
            "amount": str(amount),
            "currency": currency,
            "method": payment_method,
            "timestamp": datetime.datetime.utcnow().isoformat(),
        }

        logger.info("Processing payment %s for user %s", txn_id, user_id)

        # ❌ external dependency
        gateway_response = self._call_payment_gateway(payload)

        if gateway_response.get("status") != "success":
            raise PaymentError("Payment failed at gateway")

        return {
            "transaction_id": txn_id,
            "status": "SUCCESS",
            "processed_at": datetime.datetime.utcnow(),
            "gateway_ref": gateway_response.get("reference"),
        }


# ---- standalone util (hard to test) ----
def wait_for_settlement():
    """
    ❌ Untestable:
    - real sleep
    - no return value
    """
    time.sleep(10)
    logger.info("Settlement window passed")
