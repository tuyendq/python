# List is mutable
# List is built-in data structure in Python [whereas array is NOT]
# List stores different data types [whereas array must store SAME data type]

empty_list = []
my_list = ["listitem1", "listitem2", 1, 2, 3, True, False, 1.0, 2.0, 3.0]

# Select item(s) in list
print(my_list[0])  # first item - List index start from 0
print(my_list[1])  # second item
print(my_list[-1])  # last item
print(my_list[-2])  # second last item
print(my_list[0:2])  # first two items
print(my_list[0:3])  # first three items
print(my_list[:4])  # first four items
print(my_list[4:])  # last four items
print(my_list[::2])  # every second item
print(my_list[::-1])  # reverse list
print(my_list[::])  # copy list





list1 = ["listitem1", "listitem2"]
print(f"Check type of list1 is: {type(list1)}")
print(f"Check instance of list1: {isinstance(list1, list)}")  # should be true
print(list1)

print(list1.count(int))

list1.__str__()
list1.reverse()
print(list1)

list1.clear()
print(list1)


def deduplicate_list(input_list):
    # result = list(set(input_list))
    # result.sort()
    # return result
    return sorted(set(input_list))

test_list = ["crow", "cat", "bluejay", "cat", "woodpecker", "fox", "fox", "crow"]
print(deduplicate_list(test_list))