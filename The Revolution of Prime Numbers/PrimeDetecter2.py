# This function checks if the number(num)
# is a prime number or not
# and It is the most fastest, the most optimised and the shortest function I have created so far
# At first if number is greater than 1,
# and it is not devided by 2 and it is not to itself either,
# Then it devide this number to all prime numbers untill that number (num)
# and if remains a 0 for any of the devides, so it is devidable so it is not a prime number.

def is_prime(num):
    return all(num % i for i in range(3, int(num ** 0.5)+1, 2)) if num > 1 and num % 2 != 0 else True if num == 2 else False
