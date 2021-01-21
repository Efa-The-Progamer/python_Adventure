FiboList , Flag = [0,1] , True
"""
This Function,
at first we create a array of -1's 
to check fibonacci data's and store them in it.
Then each time we call the fibonacci function (Recursion).
Flag is for understanding that we need to create a new 
arr or we call the function recursively.
"""
def fibonacci_1(n):
    global Flag,FiboList
    if Flag:
        for i in range(n-1):
            FiboList.append(-1)
        Flag = False   
    
    if Flag == False:    
        if FiboList[n] == -1:
            FiboList[n] = fibonacci_1(n-1) + fibonacci_1(n-2) 
            return FiboList[n]   
        else:
            return FiboList[n]


print(fibonacci_1(10))

