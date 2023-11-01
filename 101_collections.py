# Collections in Python

import collections

# list: mutable 


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

# deque

# Counter

