
def is_prime(num):
    return all(num % i for i in range(3, int(num ** 0.5)+1, 2)) if num > 1 and num % 2 != 0 else True if num == 2 else False
