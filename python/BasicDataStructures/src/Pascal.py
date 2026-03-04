def pascal(n):
    prev_row = []
    for i in range(n):
        result = []
        for j in range(i + 1):
            if j == 0 or j == i:
                result.append(1)
            else:
                result.append(prev_row[j - 1] + prev_row[j])
        print(result)
        prev_row = result


pascal(5)
