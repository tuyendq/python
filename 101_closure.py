def foo():
    a = 5
    b = 10
    def bar():
        print(a)
        print(b)
    return bar

func = foo()

func()


print(f"Type of closure should be 'tuple': {type(func.__closure__)}")
print(f"Number of variables in closure tuple: {len(func.__closure__)}")
print(type(func.__closure__[0]))
print(func.__closure__[0].cell_contents)
print(func.__closure__[1].cell_contents)
