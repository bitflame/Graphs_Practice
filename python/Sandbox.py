from BasicDataStructures.src.CustomRindex import last_index_of


class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        update = [len(self.values) + 1]
        update[1:] = self.values
        update[0] = value
        self.values = update

    def print_stack(self):
        print(self.values)

    def pop(self):
        temp = self.values[0]
        self.values = self.values[1:]
        return temp

    def peek(self):
        return self.values[0]

    def isEmpty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

    def revers_index(self, item):
        reversed_values = self.values[::-1]
        return len(self.values) - self.values.index(item) - 1


stack = Stack()
print("stack should be empty, right? : ", stack.isEmpty())
stack.push("Michael")
stack.push("Zahra")
stack.push("Sakinah")
stack.push("Hassan")
# the fist name in the list ...
print('The name at the top of the list is: %s, and the length of stack is: %d' % (stack.peek(), stack.size()))
print("After adding four name: ")
stack.print_stack()
print("peeking at the top: " + stack.peek())
print("peeking at the top again: " + stack.peek())
stack.pop()
print("removed 1 name..")
stack.print_stack()
stack.pop()
print("removed another name...")
stack.print_stack()
print("stack should not be empty, right? isEmpty: ", stack.isEmpty())
list_of_names = ['Michael', 'Hassan', 'Ali', 'David']
list_of_names.pop()
list_of_names.pop(0)
# should print just David
print(list_of_names[-1])
# should print the list in reverse...
print(list_of_names[::-1])
name = 'Hassan'
print(list_of_names.index(name))
last_index_of = lambda list_of_names, name: len(list_of_names) - list_of_names[::-1].index(name) - 1
print(last_index_of(list_of_names, 'Ali'))


def someMethod(lst, name):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == name:
            return i
    return -1


f = lambda x: x * 2
print(f)
print(f(2))

numbers = [1, 2, 3, 4, 5]
names = ["Peter", "Tim", "Mike", "Tom", "Mike"]
names.append("Tom")
names.insert(1, "Carsten")
names.remove("Tom")
print(names)
names.extend(numbers)
print(names)
names.reverse()
print(names)
print(names.pop())
# should be 5
print(names.index('Tom'))
# should be 2
print(names.count('Mike'))
# list comprehension is composed of a sequence of values and a calculation rule
even = [n for n in range(10) if n % 2 == 0]
print(even)
print([(x, y) for x in range(3) for y in range(5)])
print({n: n ** 2 for n in range(10) if n % 2 == 0})


def someMethod(list, val):
    try:
        while True:
            list.remove(val)
    except (ValueError):
        pass


def methodTwo(list, val):
    while val in list:
        list.remove(val)


def thirdMethod(list, val):
    write_counter = 0
    for value in list:
        if value != val:
            list[write_counter] = value
            write_counter += 1
    return list[:write_counter]


def remove_all_v2(values, item):
    return [value for value in values if value != item]


def collect_all(values, item):
    return list(filter(lambda val: val == item, values))


print([(x, y, z) for x in range(3) for y in range(3) for z in range(3)])

mapping = {"Micha": 49, "Peter": 42, "Tom": 27}
mapping["New"] = 42
mapping.update({"Jim": 37, "John": 55})
print(mapping)
print(mapping.items())
print(mapping.keys())
print(mapping.values())
print('Micha' in mapping)
print('Micha' in mapping.keys())
# get() should not delete the item from the dictionary
print(mapping.get('Micha'))
# pop should remove Micha
mapping.pop('Micha')
print('Micha' in mapping.values())


def filter_dict(input_dict, key_value_condition):
    filtered_dict = dict()
    for key, value in input_dict.items():
        if key_value_condition((key, value)):
            filtered_dict[key] = value
    return filtered_dict


def filter_by_value(input_dict, value_condition):
    filtered_result = filter_dict(input_dict, lambda item: value_condition(item[1]))
    return filtered_result


cities_sizes = {"Cologne": 1_000_000, "Kiel": 250_000, "Bremen": 550_000, "Zurich": 400_000, "Oldenburg": 170_000}
print(filter_by_value(cities_sizes, lambda x: 200_000 <= x <= 7_000_000))
filtered_cities = filter_by_value(cities_sizes, lambda item: 200_000 <= item <= 7_000_000)
print(filtered_cities)
