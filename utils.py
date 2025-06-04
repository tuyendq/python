def kelvin_to_celsius(k):
    """
    Convert a temperature from Kelvin to Celsius.

    Parameters:
    k (float): Temperature in Kelvin. Must be greater than 0.

    Returns:
    float: Temperature in Celsius.

    Raises:
    ValueError: If the temperature in Kelvin is less than 0.

    Example:
    >>> kelvin_to_celsius(300)
    26.85
    """
    if k < 0:
        raise ValueError('Temp must be > 0 Kelvin')
    c = k - 273.15
    return c

import re
import logging
def url_friendly(string):
    """
    Convert a string to a URL-friendly format by replacing spaces with underscores.

    Parameters:
    string (str): The input string.

    Returns:
    str: The URL-friendly string.

    Example:
    >>> url_friendly("Hello World")
    'Hello_World'
    """
    string = re.sub(r'[^\w\s-]', '', string.lower())
    string = re.sub(r'[-\s]+', ' ', string).strip()
    return string.replace(' ', '_')

def validate_email(email):
    """Check email address validity."""
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    if not email_regex.match(email):
        raise ValueError(f"Invalid email address: {email}")
    return True

import time
from contextlib import contextmanager
@contextmanager
def timer():
    """Context manager to measure the elapsed time of a code block."""
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Elapsed time: {end - start} seconds")

def get_logger(name):
    """Get a logger instance with the specified name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


from contextlib import contextmanager
@contextmanager
def timer():
    """
    Context manager to measure the execution time of a block of code.

    Example:
    >>> with timer() as t:
    ...     # some code
    ...     pass
    >>> print(t.elapsed)
    0.123456789
    """
    import time
    start = time.time()
    yield TimerContext(start)
    end = time.time()
    elapsed = end - start
    print(f"Elapsed time: {elapsed:.6f} seconds")