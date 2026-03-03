class FindCommon:
    def find_common(self, values1, values2):
        if not values1 or not values2:
            raise ValueError("neither lists can be null")
        if len(vals_one) == 0 or len(values2) == 0: return []
        seen = set()
        result = []
        m = len(values1)
        n = len(values2)
        values1.sort()
        values2.sort()
        l1, l2 = 0, 0
        while l1 < m and l2 < n:
            if values1[l1] == values2[l2]:
                if values1[l1] not in seen:
                    result.append(values1[l1])
                    seen.add(values1[l1])
                l1 += 1
                l2 += 1
            elif values1[l1] < values2[l2]:
                l1 += 1
            else:
                l2 += 1
        return result


vals_one = [2, 6, 3, 9, 11]
vals_two = [15, 7, 2, 11, 9]
f = FindCommon()
print(f.find_common(vals_one, vals_two))
# test for different sizes of first list and second list
vals_one = [2]
vals_two = [11, 2]
print("expected answer [2], actual answer: ", f.find_common(vals_one, vals_two))
vals_one = [3, 1, 32]
vals_two = [22]
print("expected answer [], actual answer: ", f.find_common(vals_one, vals_two))
vals_one = [1,2,4,7,8]
vals_two = [2,3,7,9]
print("expected answer [2,7], actual answer: ", f.find_common(vals_one, vals_two))
vals_one = [1,2,7,4, 7,8]
vals_two = [7,7,3,2,9]
print("expected answer [2,7], actual answer: ", f.find_common(vals_one, vals_two))
vals_one = [2,4,6,8]
vals_two = [1,3,5,7,9]
print("expected answer [], actual answer: ", f.find_common(vals_one, vals_two))

# book's method..
def find_common_book(values1, values2):
    results = {}
    populate_from_collection1(values1, results)
    mark_if_also_in_second(values2, results)
    return remove_all_just_in_first(results)
def populate_from_collection1(values1, results):
    for elem1 in values1:
        results[elem1]=1
def mark_if_also_in_second(values2, results):
    for elem2 in values2:
        if elem2 in results:
            results[elem2]+=1
def remove_all_just_in_first(results):
    final_result = set()
    for key, value in results.items():
        if value >=2:
            final_result.add(key)
    return final_result


def bestMethod(values1, values2):
    return list(set(values1)&set(values2))