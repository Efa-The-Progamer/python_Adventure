"""
This is my fifth prime number project,
it is one of the fastest.
It will find all prime numbers between 2 and 'End'.

1. At first we create an Prime array to N
store True vlaue, and N is End + 1 == size
and another list containing 2 as our main prime list

2.we iterate all odd numbers  in range of 3 and END,
if that number's value in prime list is True,
means that we have not used it, so it is prime,
we add it to our prime list then
we make all prime list values false where we find
this number's multiplies untill the END
"""

def primeNumbers_6(End):
    size = int(End) + 1
    Prime = [True] * size
    Prime_List = [2]
    for i in range(3, size, 2):
        if Prime[i]:
            Prime_List.append(i)
            temp, index = i, 1
            while temp < size:
                Prime[temp] = False
                temp = i * index
                index += 1
    return Prime_List

print(primeNumbers_6(100000))    
