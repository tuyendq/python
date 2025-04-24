# Should read/learn "closure" first


def multiply(a, b):
    return a * b

def double_args(func):
    # return func
    # Define a new function that we can modify
    def wrapper(a, b):
        # For now, just call the original function
        # return func(a, b)
        # Modify the behavior: Call the passed function with double arguments
        return func(a * 2, b * 2)
    # Return the new function
    return wrapper

new_multiply = double_args(multiply)
print(new_multiply(1, 5))

print(multiply(1, 5))

multiply = double_args(multiply)
print(multiply(1, 5))

print(multiply.__closure__[0].cell_contents)


