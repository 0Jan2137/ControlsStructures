for n in range(1, 31):
    if n % 3 == 0 and n % 5 == 0:
        print('BINGO', end=' ')
    elif n % 3 == 0:
        print('THREE', end=' ')
    elif n % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(n, end=' ')



#najpierw sprawdzenie obydwu podzielności → BINGO
#podzielność przez 3 → THREE
#podzielność przez 5 → FIVE
#inaczej → wypisz liczbę