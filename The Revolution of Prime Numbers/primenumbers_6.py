
"""
This is my sixth prime number project,
it is the fastest function I have created untill now,
and it is also very optimised that can find lots of 
prime numbers in short period of time.
It will find all prime numbers between 2 and 'End'.

1. At first we create an Prime array of [2, 3]

2. Then until we reach the End's prime number,
we use the formula to get new prime numbers and
append it to our prime list
"""

def primeNumbers_7(End):
    Prime_List = [2, 3]
    index = 1
    while len(Prime_List) <= End - 2:
        prime_1 = 6 * index - 1
        prime_2 = 6 * index + 1
        Prime_List.append(prime_1)
        Prime_List.append(prime_2)
        index += 1
    return Prime_List
