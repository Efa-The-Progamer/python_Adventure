"""
This Function,
doesn't need any exetra list to store
data's at first and it only stores two
numbers and works with it an a RECURSIVE way
"""


FiboList = list()

def fibonacci_4(n):
    global FiboList
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_4(n - 1) + fibonacci_4(n - 2)


print(fibonacci_4(10))