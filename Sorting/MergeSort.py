import math

def mergeSort(list, p, r):
    if(r > p):
        mid = (p + r) // 2
        mergeSort(list, p, mid)
        mergeSort(list, mid + 1, r)
        Merge(list, p, mid, r)

def Merge(list, p, q, r):
    left = list[p:q + 1] + [-math.inf]
    right = list[q + 1: r + 1] + [-math.inf]
    i = j = 0 

    for index in range(p, r + 1):
        if(left[i] < right[j]):
            list[index] = right[j]
            j += 1
        else:
            list[index] = left[i]
            i += 1

def MergeSort(list):
    mergeSort(list, 0, len(list) - 1)