# for loop


# This is a simple for loop that iterates over a range of numbers
# and prints each number to the console.
for i in range(5):
    print(i)


my_dict = {"name": "John", "age": 25, "city": "New York"}
# This is a for loop that iterates over the keys of a dictionary
# and prints each key to the console.
for key in my_dict:
    print(key)
    # This prints the value associated with the current key
    print(my_dict[key])
    # This prints the key-value pair as a tuple
    print(key, my_dict[key])

# This prints the key-value pair as a tuple using the items() method
for key, value in my_dict.items():
    print(key, value)
