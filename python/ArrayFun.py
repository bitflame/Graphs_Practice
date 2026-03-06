import numpy as np
def my_method():
    my_array = np.array([[1,2,2],[3,4,5],[6,7,8]])
    print(my_array)
my_method()

def swap(values, first, second):
    values[first], values[second]=values[second], values[first]

def find(values, search_for):
    for i, current_value in enumerate(values):
        if current_value== search_for:
            return i
    return -1
