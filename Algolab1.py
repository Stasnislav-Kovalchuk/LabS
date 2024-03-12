def reversed_arr(arr):
    return arr[::-1]


def gardener_bot(array):
    arr_len = len(array)
    ready_list = []
    for i in range(arr_len):
        if i % 2 == 0:
            ready_list.extend(array[i])
        else:
            ready_list.extend(reversed_arr(array[i]))
    return ready_list


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(gardener_bot(array))
