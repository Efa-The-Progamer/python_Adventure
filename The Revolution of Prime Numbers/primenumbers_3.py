"""
This is my third prime number project,
it is not a bit fast and optimized than before.
It will find all prime numbers between 2 and 'End'.

1. At first we create an Prime array to
store 2, there is the first difference

2.we iterate all numbers in range of 3 and END,
and for each number, we divide it by all prime numbers
we got until then and that list always contains,
numbers between 2 and square of that number (i)
in this case, there is no need to divide the number(i)
to all numbers between 2 and that number,
so it is optimized.

3.If the number, divided by one of the numbers
in the prime list, so it is not a prime number
so we break out the while loop and test another number
"""

def primeNumbers_4(End):
    Prime = [2]
    for i in range(3, End, 2):
        index, flag = 0, True
        Item = Prime[0]
        while Item <= int(i ** 0.5) + 1:
            if i % Item == 0:
                flag = False
                break
            index += 1
            try:
                Item = Prime[index]
            except IndexError:
                Item = End
        if flag:
            Prime.append(i)
    return Prime


print(primeNumbers_4(1000))
