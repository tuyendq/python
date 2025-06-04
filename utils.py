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