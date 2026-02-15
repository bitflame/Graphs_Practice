def my_method(my_str):
    '''Crete a 2-D array from a string'''
    two_dem_array = []
    str_counter = 0
    for rowCounter in range(3):
        current_row = []
        for col_counter in range(3):
            if str_counter < len(my_str):
                current_row.append(my_str[str_counter])
                str_counter += 1
            else:
                current_row.append(None)
        two_dem_aray.append(current_row)
    return two_dem_aray


testStr = 'abcdefghi'
print(my_method(testStr))


