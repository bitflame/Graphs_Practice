# The original order should remain, so no sorting
def remove_duplicates(my_list):
    values = {}
    for i, val in enumerate(my_list):
        if val not in values:
            values[val]=1
    return list(values.keys())


my_list = [1, 1, 2, 3, 4, 1, 2, 3]
print(remove_duplicates(my_list))
my_list = [7, 5, 3, 5, 1]
print(remove_duplicates(my_list))
my_list = [1,1,1,1]
print(remove_duplicates(my_list))
my_list = [1, 1, 2, 3, 4, 1, 2, 3]
print(list(dict.fromkeys(my_list)))
my_list = [7, 5, 3, 5, 1]
print(list(dict.fromkeys(my_list)))