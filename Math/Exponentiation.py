def BrutePow(x, y):
    ans = 1
    for i in range(y):
        ans *= x
    return ans

def BinaryPow(x, y):
    if (y == 0):
        return 1
    if( y % 2 == 0):
        return BinaryPow(x * x, y / 2)
    else:
        return BinaryPow(x, y - 1) * x
