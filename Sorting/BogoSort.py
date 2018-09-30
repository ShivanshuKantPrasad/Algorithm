import random


def Sorted(A: list):
    for i in range(0, len(A) - 1):
        if A[i] < A[i + 1]:
            return False
    return True


def BogoSort(A: list):
    while not Sorted(A):
        x = random.randrange(0, len(A))
        y = random.randrange(0, len(A))
        A[x], A[y] = A[y], A[x]
