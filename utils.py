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
