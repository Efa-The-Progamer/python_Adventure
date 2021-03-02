def primeNumbers_6(End):
    size = int(End) + 2
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
