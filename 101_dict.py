# At the root of all things Python is a dictionary.

# Dictionary is a built-in data type in Python
# - stores key-value pairs
# - is mutable (can add, remove, or modify items after creation)
# - indexing is done by keys, not by position
# - does not allow duplicate keys


# Create an empty dictionary
cusip_lookup = {}

# Yet another way to create a dictionary
another_cusip_lookup = dict()

print(cusip_lookup)

print(another_cusip_lookup)


# Dictionary with keys and values
cusip_lookup = {'123': 'AAPL', '456': 'MSFT', '789': 'GOOG'}


# Dictionary methods
print(cusip_lookup.keys())  # Print all keys in the dictionary
print(cusip_lookup.values())  # Print all values in the dictionary
print(cusip_lookup.items())  # Print all key-value pairs in the dictionary






