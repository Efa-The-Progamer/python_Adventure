# This function checks if the number(num)
# is a prime number or not
# At first if number is greater than 1 or it is one itself,
# so it is not a prime number
# Then if it is not 2, 3, 5, it starsts to check some statmentslike:
# 1.  num - (num // 10) * 10 not in [1, 3, 7, 9]
# 2.  sum(int(i) for i in str(num)) % 3 == 0
# (sum of the numbers in the integer can not be devided by 3)
# then at last we create an iteration of prime numbers untill that number
# an if the number is one of them it is a prime number
# or if it is devided by one of the primes so it is not a prime number

# I could actually do this last part first
# but i decided to add some statements in case that
# we can find it without the iterations and have least compexity.

def primeDetecter(num):
    num = int(num)
    if num <= 1:
        return False
    elif num <= 5 and (num == 2 or num == 3 or num == 5):
        return True
    else:
        if num - (num // 10) * 10 not in [1, 3, 7, 9]:
                # or sum(int(i) for i in str(num)) % 3 == 0:
            return False
        elif sum(int(i) for i in str(num)) % 3 == 0:
            return False
        else:
            for i in range(1, int(num ** .5) + 1, 1):
                temp_1 = 6 * i - 1
                temp_2 = 6 * i + 1
                if temp_1 == num or temp_2 == num:
                    return True
                if num % temp_1 == 0 or num % temp_2 == 0:
                    return False
            return True
