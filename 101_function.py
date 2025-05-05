# Function is just another type of object in Python
# We can pass functions as arguments to other functions
# We can return functions from other functions
# We can store functions as dictionary values

# function vs method
# function: code to perform a task
# method: a function that is specific to a data type (class)

def print_hello():
    print("Hello")

def func_a():
    print('inside func_a')


def func_b(func):
    print('inside func_b')
    func()


def func_c():
    print('inside func_c')


def func_d(func):
    print('inside func_d')
    func()

# yet another example of function as argument
def has_docstring(func):
    return func.__doc__ is not None

print(has_docstring(print))
print(has_docstring(open))
print(has_docstring(has_docstring))

func_b(func_a)
func_d(func_c)

# We can also create functions on the fly
# This is called anonymous functions
# We can also pass lambda functions to other functions
# Lambda functions are used to create anonymous functions
# Lambda functions are used to create anonymous functions

list_of_functions = [func_a, func_c, open, print]
list_of_functions[3]("Call function from a list")

dict_of_functions = {'func1': func_a, 'func2': func_c, 'func3': open, 'func4': print}
dict_of_functions['func4']("Call function from a dictionary")



# Function as return values
def get_function():
    def print_me(s):
        print(s)
    # return the function 'print_me'
    return print_me

new_function = get_function()
new_function("This works! An example of 'function as return values.'")