from operator import itemgetter


def rindex(values, item):
    reversed_values = values[::-1]
    return len(values) - reversed_values.index(item)-1
last_index_of = lambda values, item: len(values) - values[::-1].index(itemgetter)-1

def triplets():
    print([(x, y, z) for x in range(3) for y in range(3) for z in range(3)])
triplets()

# examples of set comprehension and dictionary comprehension. Notice there are {} around not []s
{n for n in range(10) if n % 2 != 0}
{n: n ** 2 for n in range(10) if n % 2 ==0 }
