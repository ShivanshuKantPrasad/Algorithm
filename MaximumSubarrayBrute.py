def MaximumSubarray(list):
    maxSum = 0
    besti = bestj = 0
    for i in range(0, len(list)):
        currentSum = 0
        for j in range(i, len(list)):
            currentSum += list[j]
            if currentSum > maxSum:
                maxSum = currentSum
                besti, bestj = i, j
    return besti, bestj

list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(MaximumSubarray(list))