"""
This Function,
doesn't need any exetra list to store
data's at first and it only stores two
numbers and works with it an a RECURSIVE way
And It is THE FASTEST Fibonacci function i've writen until now
"""


def fibonacci_5(n):
    fibolist = [1, 0]
    for i in range(n-1):
        fibolist[0] += fibolist[1]
        fibolist[1] = fibolist[0] - fibolist[1]
    return fibolist[0]

