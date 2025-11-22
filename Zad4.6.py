# Calculates the sum of integer numbers in the range <5,10>
sum = 0

# Zmieniamy zakres na <5, 11), aby uwzględnić liczbę 10
for i in range(5, 11):
    sum += i  # Używamy operatora += zamiast sum = sum + i

print(f'Sum is {sum}')