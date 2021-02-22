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
