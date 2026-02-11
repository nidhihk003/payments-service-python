import os
import time
import random
import signal
import pytest


# -----------------------------
# GLOBAL SIDE EFFECT (UNTESTABLE)
# -----------------------------
signal.signal(signal.SIGTERM, lambda *_: None)


def test_payment_env_variable_must_exist():
    """
    ❌ FAIL-PRONE
    Reason:
    - Depends on environment variable
    - CI usually does NOT set this
    """
    assert os.environ["PAYMENT_GATEWAY_SECRET"] == "expected-secret"


def test_payment_processing_completes_within_1ms():
    """
    ❌ FAIL-PRONE
    Reason:
    - Time-based assertion
    - CI machines are slower / unpredictable
    """
    start = time.time()
    time.sleep(0.01)  # 10ms sleep
    duration = time.time() - start

    assert duration < 0.001  # impossible


def test_random_transaction_id_is_deterministic():
    """
    ❌ UNTESTABLE
    Reason:
    - Uses randomness without seeding
    """
    txn_id = random.randint(1000, 9999)
    assert txn_id == 1234


def test_os_specific_path_exists():
    """
    ❌ FAIL-PRONE
    Reason:
    - OS-dependent path
    - Will fail on Linux CI
    """
    assert os.path.exists("C:\\Payments\\config\\prod.yaml")


def test_signal_handling_does_not_exit_process():
    """
    ❌ UNTESTABLE
    Reason:
    - Signal behavior depends on process / runner
    - Pytest cannot reliably simulate this
    """
    os.kill(os.getpid(), signal.SIGTERM)
    assert True  # Will never reach here
