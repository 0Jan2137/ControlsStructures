# print first 20 Fibonacci numbers

a = 0   # first term
b = 1   # second term

print(a, b, end=' ')

for _ in range(18):      # we already printed 2 numbers, need 18 more
    c = a + b
    print(c, end=' ')
    a = b
    b = c



#start: 0 i 1
#kolejne liczby = suma dwóch poprzednich
#wypisanie pierwszych 20 elementów