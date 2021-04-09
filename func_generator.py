#!/usr/bin/env python
# File: func_generator.py
# Build generator function

def get_lengths(input_list):
    """Generator function that yields the length of string in input_list
    """

    for item in input_list:
        yield len(item)

# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

for item in get_lengths(lannister):
    print(item)
