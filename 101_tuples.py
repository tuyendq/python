# tuple is one of four built-in collection data types in Python (list, set, dictionary)
# tuple is ordered, immutable, allow duplicate


print("Play with tuple")
tuple1 = ('apple', 'kiwi')
print(tuple1)

# insert item to tuple
def insert_item(my_tuple, new_value, index):
    # x = list(my_tuple)
    # x.insert(index, new_value)
    # return tuple(x)
    
    return my_tuple[:index] + (new_value,) + my_tuple[index:]


update_tuple = insert_item(tuple1,"lemon", 1)
print(update_tuple)