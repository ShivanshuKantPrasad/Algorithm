def MaximumSubarray(list):
    maxSum = float("-inf")
    minSum = 0
    maxLeft = maxRight = 0
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
        newSum = sum - minSum 
        if(newSum > maxSum):
            maxSum = newSum
            maxRight = i
        if(newSum < minSum):
            minSum = newSum
            maxLeft = i

        
    return maxLeft + 1, maxRight
