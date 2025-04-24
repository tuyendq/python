x = 25

def foo(value):
    def bar():
        print(value)
    return bar

my_func = foo(x)

# Let's remove the global 'x' variable
del(x)
# Then try printing the deleted global 'x' variable
try:
    print(x)
except NameError as e:
    print(e)


my_func()


print(my_func.__closure__)
print(my_func.__closure__[0].cell_contents)