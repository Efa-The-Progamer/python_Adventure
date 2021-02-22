"""
This is my first prime number project,
it is not fast but it will work properly.
It will find all prime numbers between 2 and 'End'.

1. At first we create an Prime array to 
store 2, 3 and all numbers between 3 and 'End'
if number is odd and it is not divided by 3

2. Then we create a copy of Prime,
because we want to iterate through prime elements
but deleting an item from prime itself will cause error

3.we iterate through prime and for each item 
until we reach that item itself, we divide it by all 
other numbers if it's remain is zero,
so it is not a prime number
so we remove it from prime list
"""

def primeNumbers_1(End):
    Prime = [2, 3] + [p for p in range(3, End, 2) if p % 3 != 0]
    Second_Prime = Prime.copy()
    for i in Second_Prime:
        for j in Second_Prime:
            if i > j:
                if i % j == 0:
                    try:
                        Prime.remove(i)
                    except ValueError:
                        continue
            else:
                break
    return Prime


print(primeNumbers_1(10))    
