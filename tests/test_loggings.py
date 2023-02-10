def test_check_loggings():
  print("Should return true")
  assert 4 == 1 + 3
  print("Should PASSED if logging is installed")
  try:
    import logging
    assert isinstance(logging.getLogger(), logging.RootLogger)
  except ModuleNotFoundError:
    print("FAILED: 'logging'not installed")
