hours = int(input('Enter number of parking hours: '))

if 1 <= hours <= 2:
    fee = 5
elif 3 <= hours <= 6:
    fee = 15
else:
    fee = 20

print('Parking fee:', fee, 'PLN')



#sprawdzenie przedziału 1–2 h → 5 PLN
#sprawdzenie przedziału 3–6 h → 15 PLN
#wszystkie >6 h → 20 PLN