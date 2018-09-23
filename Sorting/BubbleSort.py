def BubbleSort(list):
    for i in range(0, len(list)):
        for j in range(0, i):
            if(list[i] > list[j]):
                list[i], list[j] = list[j], list[i]