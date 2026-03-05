from operator import itemgetter


def value_count(values):
    frequencies = [0]*10
    for val in values:
        frequencies[val]+=1
    return frequencies
def print_results(frequencies):
    for i in range(len(frequencies)):
        print(f'{i}= {frequencies[i]}')
values = [1,2,3,4,4,4,3,3,2,4]
print_results(value_count(values))
my_dict = {3: 6, 2: 4, 1:1}
print(my_dict)
print(sorted(my_dict.items(), key=itemgetter(1),reverse=True))
for i in my_dict.items():
    print(i)

