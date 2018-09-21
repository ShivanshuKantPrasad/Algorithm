def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key

if __name__ == "__main__":
    numbers = [10, 27, 8, 23, 58, 42, 56, 12]
    insertionsort(numbers)
    print(numbers)