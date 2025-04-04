# Function is just another type of object in Python, such as integer, string...
def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five,10))