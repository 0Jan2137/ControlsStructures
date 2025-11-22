# Print lottery coupon numbers from 1 to 49 in rows

start = 1
while start <= 7:              # 7 rows
    num = start
    for _ in range(7):         # 7 numbers per row
        print(num, end=' ')
        num += 7
    print()
    start += 1



#każda linia zaczyna się od innej liczby: 1…7
#w każdej linii wypisujemy 7 liczb
#kolejne liczby w wierszu tworzymy dodając +7
#razem tworzy układ jak na kuponie lotto (1–49 w kolumnach)