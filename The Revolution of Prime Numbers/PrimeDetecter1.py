
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
