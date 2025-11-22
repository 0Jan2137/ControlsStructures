correct_pin = "0805"
attempts = 0

while attempts < 3:
    pin = input("Enter the PIN code: ")

    if pin == correct_pin:
        print("Correct PIN. Access granted.")
        break
    else:
        print("Incorrect...")
        attempts += 1

if attempts == 3:
    print("Sorry, your payment card has been blocked.")



#ustawienie prawidłowego PIN-u "0805"
#pętla max 3 razy
#jeśli PIN poprawny → przerwij pętlę
#jeśli 3 błędy → komunikat o blokadzie