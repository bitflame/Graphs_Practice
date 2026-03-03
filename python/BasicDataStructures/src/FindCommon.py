class FindCommon:
    def find_common(self, values1, values2):
        if not values1 or not values2:
            raise ValueError("neither lists can be null")
        if len(vals_one) == 0 or len(values2) == 0: return []
        result = []
        m = len(values1)
        n = len(values2)
        values1.sort()
        values2.sort()
        l1, l2 = 0, 0
        while l1 < m and l2 < n:
            if values1[l1] == values2[l2] and result.count(values1[l1])==0:
                result.append(values1[l1])
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