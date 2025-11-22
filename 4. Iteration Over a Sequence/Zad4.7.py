# Calculates the sum of even numbers in the range <1,10>
sum = 0

for i in range(1, 11):
    # Jeśli liczba NIE jest parzysta (reszta z dzielenia != 0), pomiń ją
    if not i % 2 == 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')