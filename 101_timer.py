import time

def timer(func):
    """
    A decorator that measures the execution time of a function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that prints the execution time.
    """
    # Define the wrapper function to return
    def wrapper(*args, **kwargs):
        # When wrapper is called, get the current time
        start_time = time.time()
        # Call the decorated function and store the result
        result = func(*args, **kwargs)
        # Get the total time it took to execute the function, and print it
        total_time = time.time() - start_time
        print(f"Function '{func.__name__}' took {total_time:.4f} seconds to execute")
    
    return wrapper

def memoize(func):
    """
    A decorator that caches the results of a function to avoid redundant calculations.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that caches results.
    """
    # Store the results in a dictionary
    # The key is the arguments passed to the function
    cache = {}
    
    def wrapper(*args, **kwargs):
        kwargs_key = tuple(sorted(kwargs.items()))
        # When wrapper is called, check if the result is already cached
        if (args, kwargs_key) not in cache:
            cache[(args, kwargs_key)] = func(*args, **kwargs)
        return cache[(args, kwargs_key)]
    
    return wrapper

# Example usage of the timer decorator
@timer
def sleep_n_seconds(n):
    """
    Sleeps for n seconds.

    Args:
        n (int): The number of seconds to sleep.
    """
    time.sleep(n)

sleep_n_seconds(5)

# Example usage of the memoize decorator
@memoize
def slow_function(a, b):
    sleep_time = 5
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)
    return a * b

# Test the slow function with memoization
print(slow_function(2, 3))
print(slow_function(2, 3))  # This should be faster due to memoization
