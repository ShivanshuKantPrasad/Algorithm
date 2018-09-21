def horner(coefficients: list, x: float):
    res = 0
    for coefficient in reversed(coefficients):
        res = x * res + coefficient
    return res

coeffs = [2, 3] #  3x + 2
print(horner(coeffs, 2))