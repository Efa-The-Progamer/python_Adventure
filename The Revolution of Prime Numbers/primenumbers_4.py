
def primeNumbers_4(End):
    temp_prime = [p for p in range(5, End, 2) if p % 3 != 0]
    Prime = [2, 3]
    for i in temp_prime:
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


