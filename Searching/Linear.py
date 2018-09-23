def search(list, query):
    for i in range( 0, len(list)):
        if query == list[i]:
            return i
    return None