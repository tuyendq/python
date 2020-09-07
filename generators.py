#!/usr/bin/env python
# File: generators.py

a_list = [num ** 2 for num in range(10)]

print(a_list)

a_gen = (num ** 2 for num in range(10))
print(a_gen)

# Print element line by line
for num in a_gen:
    print(num)

# Print as list
a_gen = (num ** 2 for num in range(10))
print(list(a_gen))

# Lazy print
a_gen = (num ** 2 for num in range(10))
print(next(a_gen))
print(next(a_gen))
print(next(a_gen))


def num_sequence(n):
    """Generate values from 0 to n."""

    i = 0
    while i < n:
        yield i
        i += 1

seq = num_sequence(5)
print(list(seq))
