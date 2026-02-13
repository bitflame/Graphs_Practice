def hex_to_dec(number):
    map = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    result = 0
    for index, num in enumerate(reversed(number)):
        if num.isalpha():
            result += map.get(num.tolower()) * 16 ** index
        else:
            result += int(num) * 16 ** index
    return result


print(f'{hex_to_dec()}')
