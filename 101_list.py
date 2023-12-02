# List is mutable
# List is built-in data structure in Python [whereas array is NOT]
# List stores different data types [whereas array must store SAME data type]

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
    result = list(set(input_list))
    result.sort()
    return result

test_list = ["crow", "cat", "bluejay", "cat", "woodpecker", "fox", "fox", "crow"]
print(deduplicate_list(test_list))