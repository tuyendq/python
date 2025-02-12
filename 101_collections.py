# Collections in Python

# 4 built-in collection data types in Python: list, tuple, set, dictionary

import collections

# list: mutable 
list1 = ['list_item1', 'list_item2', 'list_item3']
print(list1)
print(type(list1))
print(isinstance(list1, list))

# tuple: fixed (immutable)

# set: distinct/unique value

# dictionary: key:value pair

# namedtuple
Point = collections.namedtuple("Point", "x y")
p1 = Point(5, 10)
p2 = Point(10, 20)
print(p1, p2)
print(p1.x, p2.y)

# _replace 
p2 = p2._replace(y=100)
print(p2)



# defaultdict

# deque - double-ended queu
deck1 = collections.deque('abcdef')
print(deck1)
for el in deck1:
    print(el.upper())
    
import string
deck2 = collections.deque(string.ascii_lowercase)
print(deck2)
print(f"Length of deck2 is: {len(deck2)}")




# Counter

