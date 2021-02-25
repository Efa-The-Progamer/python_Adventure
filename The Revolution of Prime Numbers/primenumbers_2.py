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
