import math


# def mergeSort(alist):
#     print("Splitting ",alist)
#     if len(alist)>1:
#         mid = len(alist)//2
#         lefthalf = alist[:mid]
#         righthalf = alist[mid:]

#         mergeSort(lefthalf)
#         mergeSort(righthalf)

#         i=0
#         j=0
#         k=0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 alist[k]=righthalf[j]
#                 j=j+1
#             k=k+1

#         while i < len(lefthalf):
#             alist[k]=lefthalf[i]
#             i=i+1
#             k=k+1

#         while j < len(righthalf):
#             alist[k]=righthalf[j]
#             j=j+1
#             k=k+1
#     print("Merging ",alist)

def mergeSort(list, p, r):
    if(r > p):
        mid = (p + r) // 2
        mergeSort(list, p, mid)
        mergeSort(list, mid + 1, r)
        Merge(list, p, mid, r)

def Merge(list, p, q, r):
    left = list[p:q + 1] + [math.inf]
    right = list[q + 1: r + 1] + [math.inf]
    i = j = 0 

    for index in range(p, r + 1):
        if(left[i] > right[j]):
            list[index] = right[j]
            j += 1
        else:
            list[index] = left[i]
            i += 1



alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist, 0, len(alist) - 1)
print(alist)
