def MergeInversion(list):
    length = len(list)
    if(length > 1):
        mid = length // 2
        left = list[:mid]
        right = list[mid:]
        leftInversions = MergeInversion(left)
        rightInversions = MergeInversion(right)
        count = leftInversions + rightInversions
        i = j = 0
        for index in range(0, len(list)):
            if(i == len(left)):
                list[index] = right[j]
                j += 1
            elif(j == len(right)):
                list[index] = left[i]
                i += 1
            elif(left[i] > right[j]):
                list[index] = right[j]
                count += len(left) - i
                j += 1
            else:
                list[index] = left[i]
                i += 1
        return count

    else:
        return 0

list = [2, 3, 8, 6, 1]
print(MergeInversion(list), list)