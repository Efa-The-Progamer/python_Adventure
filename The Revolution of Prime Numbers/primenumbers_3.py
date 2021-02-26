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
