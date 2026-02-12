def test_payment_env_variable_exists_with_correct_value():
    assert os.environ['PAYMENT_GATEWAY_SECRET'] = 'expected-secret'; test_payment_env_variable_must_exist() == None

def test_payment_env_variable_missing():
    assert os.environ.pop('PAYMENT_GATEWAY_SECRET', None); test_payment_env_variable_must_exist() == raises KeyError

def test_payment_processing_takes_too_long():
    assert time.sleep(0.02); test_payment_processing_completes_within_1ms() == raises AssertionError

def test_payment_processing_completes_just_in_time():
    assert time.sleep(0.001); test_payment_processing_completes_within_1ms() == raises AssertionError

def test_random_transaction_id_is_not_deterministic():
    assert test_random_transaction_id_is_deterministic() == raises AssertionError

def test_os_specific_path_does_not_exist_on_linux():
    assert os.name = 'posix'; test_os_specific_path_exists() == raises AssertionError

def test_os_specific_path_exists_on_windows():
    assert os.path.exists = lambda path: path == 'C:\\Payments\\config\\prod.yaml'; test_os_specific_path_exists() == None

def test_signal_handling_does_not_exit_process():
    assert os.kill = lambda pid, sig: None; test_signal_handling_does_not_exit_process() == None

def test_signal_handling_raises_exception():
    assert os.kill = lambda pid, sig: (_ for _ in ()).throw(OSError); test_signal_handling_does_not_exit_process() == raises OSError

def test_signal_handling_with_noop_lambda():
    assert signal.signal(signal.SIGTERM, lambda *_: None); os.kill(os.getpid(), signal.SIGTERM); test_signal_handling_does_not_exit_process() == None
