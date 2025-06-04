# Two types of arguments: positional and keyword arguments
# *args: Arbitrary arguments
# **kwargs: Arbitray keyword arguments key=value

import sys

def sum_all(*args):
    """Sum all arguments. 
    An example of arbitrary argument.
    * [asterisk] means convert all arguments into a tuple.
    """
    sum = 0
    for n in args:
        sum += n
    return sum

def concat(*args):
  """Yet another example using arbitrary argument *args."""
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))

def ya_concat(**kwargs):
  """Yet another example using arbitrary keyword argument **kwargs."""
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(ya_concat(begin="Python", middle="is", end="great!"))

# Another example of using arbitrary keyword argument **kwargs
def print_kwargs(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key} = {value}")
# Call the function
print_kwargs(name="Alice", age=30, city="New York")

def main():
    print(f'Example to print out arguments')
    for i in range(0, len(sys.argv)):
        print(f'Argument {i}: {sys.argv[i]}')

    number = int(input('Enter an integer: '))
    print('Sum all integer from 0 to {} is: '.format(number), end='')
    print(sum(range(number)))

if __name__ == "__main__":
    main()
