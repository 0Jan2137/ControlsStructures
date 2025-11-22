N = int(input("How many prime numbers do you want to display? "))

count = 0        # how many primes found
number = 2       # first number to check

print("Prime numbers:", end=" ")

while count < N:
    # check if 'number' is prime
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
        count += 1

    number += 1



#pobranie N
#sprawdzanie kolejnych liczb od 2 wzwyż
#liczba jest pierwsza jeśli nie dzieli się przez żadne i od 2 do number-1
#wypisywanie dopóki nie znajdziemy N liczb pierwszych