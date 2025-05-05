import utils

def test_utils():
    # Test kelvin_to_celsius function
    assert kelvin_to_celsius(300) == 26.85
    assert kelvin_to_celsius(0) == -273.15
    try:
        kelvin_to_celsius(-1)
    except ValueError as e:
        assert str(e) == 'Temp must be > 0 Kelvin'

    # Test url_friendly function
    assert url_friendly("  Hello # World  ") == "hello_world"
    assert url_friendly("Hello-World") == "hello_world"

