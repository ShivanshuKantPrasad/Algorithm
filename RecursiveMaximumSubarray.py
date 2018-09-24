def FindMaxCrossingSubarray(list, low, mid, high):
    leftSum = float("-inf")
    sum = maxLeft = 0
    for i in range(mid, low, -1):
        sum += list[i]
        if(sum > leftSum):
            leftSum = sum
            maxLeft = i

    rightSum = float("-inf")
    sum = maxRight = 0
    for j in range(mid, high):
        sum += list[j]
        if(sum > rightSum):
            rightSum = sum
            maxRight = j
    return(maxLeft, maxRight, leftSum + rightSum)


def FindMaximumSubarray(list, low, high):
    if(high == low):
        return (low, high, list[low])
    else:
        mid = (high + low) // 2
        left = FindMaximumSubarray(list, low, mid)
        right = FindMaximumSubarray(list, mid + 1, high)
        cross = FindMaxCrossingSubarray(list, low, mid, high)
        return max(left, right, cross, key = lambda self: self[2])

def MaximumSubarray(list):
    low, high, sum = FindMaximumSubarray(list, 0, len(list) - 1)
    return low, high