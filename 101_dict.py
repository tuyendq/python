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
# - clear() - removes all items from the dictionary
# - copy() - returns a shallow copy of the dictionary
# - fromkeys() - creates a new dictionary with keys from the given iterable and values set to the specified value
# - get() - returns the value for the specified key, or None if the key does not exist
# - items() - returns a view object that displays a list of a dictionary's key-value tuple pairs
# - keys() - returns a view object that displays a list of all the keys in the dictionary
# - pop() - removes the specified key and returns the corresponding value
# - popitem() - removes the last inserted key-value pair and returns it as a tuple
# - setdefault() - returns the value of the specified key, if the key does not exist, insert the key with the specified value
# - update() - updates the dictionary with the specified key-value pairs
# - values() - returns a view object that displays a list of all the values in the dictionary

print(cusip_lookup.values())  # Print all values in the dictionary
print(cusip_lookup.items())  # Print all key-value pairs in the dictionary




# Operations on dictionaries
# in, not in - check if a key exists in the dictionary

