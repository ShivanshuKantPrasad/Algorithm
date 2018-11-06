def brute_pow(x, y):
    ans = 1
    for i in range(y):
        ans *= x
    return ans

