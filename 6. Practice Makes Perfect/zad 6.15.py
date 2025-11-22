ean = input('Enter EAN-13 article number: ')

# check if length is exactly 13
if len(ean) == 13:
    print('Article number is correct')
    
    # check if manufactured in Poland (starts with 590)
    if ean.startswith('590'):
        print('Article manufactured in Poland')
else:
    print('Incorrect article number')



#sprawdzenie długości kodu (len(ean) == 13)
#komunikat: poprawny / niepoprawny
#jeśli poprawny → sprawdzenie prefiksu 590
#startswith('590') oznacza produkcję w Polsce