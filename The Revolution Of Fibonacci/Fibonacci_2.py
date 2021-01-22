fibolist = [0, 1]
"""
This Function,
at first we create a array of -1's 
to check fibonacci data's and store them in it.
Then each time we call the fibonacci function (Recursion).
Flag is for understanding that we need to create a new 
arr or we call the function recursively.
it is a little better thatn first one
"""
def Fibonacci_2(n, flag = True):
    global fibolist
    if not flag:
        fibolist = [0,1]+[-1 for i in range(n)]
        flag = False

    if fibolist[n] == -1:
        fibolist[n] = Fibonacci_1(n-1) + Fibonacci_1(n-2)
    return fibolist[n]

