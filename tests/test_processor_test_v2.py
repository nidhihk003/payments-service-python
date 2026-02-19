from .src.payments.processor import processor

import pytest

def test_process_payment_successful_card_payment():
    import os
    from decimal import Decimal
    from unittest.mock import patch
    os.environ['PAYMENT_GATEWAY_URL'] = 'https://api.fakepay.com/charge'
    os.environ['PAYMENT_API_KEY'] = 'hardcoded-key'
    from src.payments.processor import PaymentProcessor
    processor = PaymentProcessor()
    with patch('src.payments.processor.PaymentProcessor._call_payment_gateway', return_value={'status': 'success', 'reference': 'ref-12345'}): result = processor.process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card')
    assert result == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': 'ref-12345'}

def test_process_payment_successful_wallet_payment():
    import os
    from decimal import Decimal
    from unittest.mock import patch
    os.environ['PAYMENT_GATEWAY_URL'] = 'https://api.fakepay.com/charge'
    os.environ['PAYMENT_API_KEY'] = 'hardcoded-key'
    from src.payments.processor import PaymentProcessor
    processor = PaymentProcessor()
    with patch('src.payments.processor.PaymentProcessor._call_payment_gateway', return_value={'status': 'success', 'reference': 'ref-67890'}): result = processor.process_payment(user_id='user123', amount=Decimal('200.00'), currency='USD', payment_method='wallet')
    assert result == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': 'ref-67890'}

def test_process_payment_with_negative_amount():
    with pytest.raises(ValueError):
        from decimal import Decimal
        from src.payments.processor import PaymentProcessor
        processor = PaymentProcessor()
        processor.process_payment(user_id='user123', amount=Decimal('-100.00'), currency='USD', payment_method='card')

def test_process_payment_with_zero_amount():
    with pytest.raises(ValueError):
        from decimal import Decimal
        from src.payments.processor import PaymentProcessor
        processor = PaymentProcessor()
        processor.process_payment(user_id='user123', amount=Decimal('0.00'), currency='USD', payment_method='card')

def test_process_payment_with_unsupported_currency():
    with pytest.raises(ValueError):
        from decimal import Decimal
        from src.payments.processor import PaymentProcessor
        processor = PaymentProcessor()
        processor.process_payment(user_id='user123', amount=Decimal('100.00'), currency='GBP', payment_method='card')

def test_process_payment_gateway_failure():
    with pytest.raises(PaymentError):
        import os
        from decimal import Decimal
        from unittest.mock import patch
        os.environ['PAYMENT_GATEWAY_URL'] = 'https://api.fakepay.com/charge'
        os.environ['PAYMENT_API_KEY'] = 'hardcoded-key'
        from src.payments.processor import PaymentProcessor
        processor = PaymentProcessor()
        from src.payments.processor import PaymentError
        with patch('src.payments.processor.PaymentProcessor._call_payment_gateway', side_effect=PaymentError('Gateway error')): processor.process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card')

def test_process_payment_missing_payment_gateway_url():
    with pytest.raises(PaymentError):
        import os
        from decimal import Decimal
        from unittest.mock import patch
        os.environ['PAYMENT_API_KEY'] = 'hardcoded-key'
        from src.payments.processor import PaymentProcessor
        processor = PaymentProcessor()
        from src.payments.processor import PaymentError
        os.environ.pop('PAYMENT_GATEWAY_URL')
        with patch('src.payments.processor.PaymentProcessor._call_payment_gateway', side_effect=PaymentError('Gateway error')): processor.process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card')

def test_process_payment_missing_api_key():
    with pytest.raises(PaymentError):
        import os
        from decimal import Decimal
        from unittest.mock import patch
        os.environ['PAYMENT_GATEWAY_URL'] = 'https://api.fakepay.com/charge'
        from src.payments.processor import PaymentProcessor
        processor = PaymentProcessor()
        from src.payments.processor import PaymentError
        os.environ.pop('PAYMENT_API_KEY')
        with patch('src.payments.processor.PaymentProcessor._call_payment_gateway', side_effect=PaymentError('Gateway error')): processor.process_payment(user_id='user123', amount=Decimal('100.00'), currency='USD', payment_method='card')

def test_generate_transaction_id():
    from src.payments.processor import PaymentProcessor
    processor = PaymentProcessor()
    assert result = processor._generate_transaction_id() == txn-<timestamp>-<random>

def test_call_payment_gateway_success():
    import os
    os.environ['PAYMENT_GATEWAY_URL'] = 'https://api.fakepay.com/charge'
    os.environ['PAYMENT_API_KEY'] = 'hardcoded-key'
    from src.payments.processor import PaymentProcessor
    processor = PaymentProcessor()
    payload = {'transaction_id': 'txn-1234', 'user_id': 'user123', 'amount': '100.00', 'currency': 'USD', 'method': 'card', 'timestamp': '2023-10-05T00:00:00'}
    from unittest.mock import patch
    assert with patch('requests.post', return_value=type('obj', (object,), {'status_code': 200, 'json': lambda: {'status': 'success', 'reference': 'ref-12345'}})): result = processor._call_payment_gateway(payload) == {'status': 'success', 'reference': 'ref-12345'}

def test_process_payment_with_eur_currency():
    import os
    from decimal import Decimal
    from unittest.mock import patch
    os.environ['PAYMENT_GATEWAY_URL'] = 'https://api.fakepay.com/charge'
    os.environ['PAYMENT_API_KEY'] = 'hardcoded-key'
    from src.payments.processor import PaymentProcessor
    processor = PaymentProcessor()
    with patch('src.payments.processor.PaymentProcessor._call_payment_gateway', return_value={'status': 'success', 'reference': 'ref-54321'}): result = processor.process_payment(user_id='user123', amount=Decimal('150.00'), currency='EUR', payment_method='card')
    assert result == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': 'ref-54321'}

def test_process_payment_with_inr_currency():
    import os
    from decimal import Decimal
    from unittest.mock import patch
    os.environ['PAYMENT_GATEWAY_URL'] = 'https://api.fakepay.com/charge'
    os.environ['PAYMENT_API_KEY'] = 'hardcoded-key'
    from src.payments.processor import PaymentProcessor
    processor = PaymentProcessor()
    with patch('src.payments.processor.PaymentProcessor._call_payment_gateway', return_value={'status': 'success', 'reference': 'ref-98765'}): result = processor.process_payment(user_id='user123', amount=Decimal('300.00'), currency='INR', payment_method='card')
    assert result == {'transaction_id': 'txn-<timestamp>-<random>', 'status': 'SUCCESS', 'processed_at': '<datetime>', 'gateway_ref': 'ref-98765'}
