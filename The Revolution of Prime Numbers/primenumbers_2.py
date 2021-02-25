"""
This is my second prime number project,
it is not fast and optimized but it will work properly.
It will find all prime numbers between 2 and 'End'.

1. At first we create an Prime array to
store 2, 3 and all numbers between 3 and 'End'
if number is odd and it is not divided by 3

2.we iterate through prime and for each item
until we reach that item itself,
we discover multiples of that number
then remove it from the prime list
so only prime numbers remain
"""

def primeNumbers_2(End):
    Prime = [2, 3] + [p for p in range(5, End, 2) if p % 3 != 0]
    P_Length = int(len(Prime) ** 0.5)
    for i in Prime[2:P_Length:1]:
        p = 5
        j = p * i
        while j <= End:
            try:
                Prime.remove(j)
            except ValueError:
                pass

            p += 2
            j = p * i
    return Prime


print(primeNumbers_2(100))
