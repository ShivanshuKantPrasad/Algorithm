def inversion(list: list):
    res = 0
    for i in range(0, len(list)):
        for j in range(0, i):
            if list[i] > list[j]:
                res += 1
    return res