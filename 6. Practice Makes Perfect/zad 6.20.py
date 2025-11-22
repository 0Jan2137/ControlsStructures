number = int(input('Enter decimal number: '))

original = number
binary_digits = ""

while number > 0:
    remainder = number % 2
    binary_digits = str(remainder) + binary_digits
    number = number // 2

print(f"{original}(10) = {binary_digits}(2)")


#pobranie liczby dziesiętnej
#w pętli: dzielenie przez 2 i zbieranie reszt
#reszty dopisujemy od przodu → odwrócony wynik
#wypisanie w formacie X(10) = Y(2)