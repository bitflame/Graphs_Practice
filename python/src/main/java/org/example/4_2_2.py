def join(values, delimiter):
    result = ''
    for val in values:
        result+=val+delimiter
    return result

values = ["hello", "World", "message"]
delimiter = "+++"
print(f'{join(values, delimiter)}')

