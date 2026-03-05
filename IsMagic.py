def is_magic(values):
    if len(values)%3!=0:
        raise ValueError('Not a triangle. ',len(values), 'must be a factor of 3.')
    side_length = 1+len(values)//3
    values_with_loop=list(values)
    values_with_loop.append(values[0])
    side1 = values_with_loop[0: side_length]
    side2 = values_with_loop[side_length-1: side_length*2-1]
    side3 = values_with_loop[(side_length-1)*2:side_length*3-2]
    return compare_sum_of_sides(side1, side2, side3)

def compare_sum_of_sides(side1, side2, side3):
    sum1 = sum(side1)
    sum2 = sum(side2)
    sum3 = sum(side3)
    return sum1==sum2 and sum2 == sum3
values = [1,5,3,4,2,6]
print(is_magic(values))