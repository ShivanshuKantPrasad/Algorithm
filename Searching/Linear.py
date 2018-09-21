def search(list, query):
    for i in range( 0, len(list)):
        if query == list[i]:
            return i
    return None

if __name__ == "__main__":
    list = [20, 30, 25, 14, 25]
    print(search(list, 25))
    print(search(list, 2))