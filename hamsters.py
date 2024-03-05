def max_hamsters(s, hamsters):
    result = 0
    c = len(hamsters)
    for i in range(0, c):
        temp_array = sorted([x[0] + x[1] * i for x in hamsters])
        temp_sum = 0
        for j in range(i):
            temp_sum += temp_array[j]
        if temp_sum <= s:
            result = i + 1
        else:
            break
    return result
