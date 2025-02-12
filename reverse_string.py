def reverse_string(string):
  """Reverse a string
  Args:
    string (str): string to be reversed
  Returns:
    str
  Raised:
    TypeError
    ValueError
  """
  if (isinstance(string, str) == False):
    raise TypeError("Input must be a string")
  elif (len(string) == 0):
    raise ValueError("Input must not be empty")
  return string[::-1]

print("Hello World")
print(reverse_string("Hello World"))
print("Madam")
print(reverse_string("Madam"))

# Should raise ValueError
# print(reverse_string(""))

# Should raise TypeError
# print(reverse_string(123))  

# Should raise TypeError
# print(reverse_string([1, 2, 3, 4, 5]))  


