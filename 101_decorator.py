def add_hello(func):
    """Decorator that adds a greeting before calling the function."""
    def wrapper(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)
    return wrapper
# This line should be removed to allow the decorator to work correctly

@add_hello
def print_message(message):
    """Print a message."""
    print(message)

print_message("How are you?")
print(print_message.__doc__)
print(add_hello.__doc__)
print(print_message.__closure__[0].cell_contents)