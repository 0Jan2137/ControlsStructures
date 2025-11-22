amount = int(input('Enter the amount in PLN: '))

coins_5 = amount // 5
amount = amount % 5

coins_2 = amount // 2
amount = amount % 2

coins_1 = amount

print('The amount in coins:')
print('5 PLN coins:', coins_5)
print('2 PLN coins:', coins_2)
print('1 PLN coins:', coins_1)



#najpierw bierzemy jak najwięcej monet 5 PLN
#resztę dzielimy na monety 2 PLN
#reszta po 2 PLN to liczba monet 1 PLN
#metoda zachłanna → najmniej monet