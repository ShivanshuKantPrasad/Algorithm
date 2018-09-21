def Euclidean(a: int, b: int):
    return b if a % b == 0 else Euclidean(b, a % b)
    
print(Euclidean( 5, 2))  
