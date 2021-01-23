"""
This Function,
doesn't need any exetra list to store
data's at first and it only stores two 
numbers and works with it
"""

def fibonacci_3(n):
    a,b = 1,0
    FiboList = [1]
    for i in range(n-1):
        a = a + b
        b = a - b
        FiboList.append(a)
    return FiboList    


"""
Same Function with WHILE this time
"""
def fibonacci_3(n):
    a,b = 1,0
    FiboList = [1]
    while len(FiboList) != n:
        a = a + b
        b = a - b
        FiboList.append(a)
    return FiboList

