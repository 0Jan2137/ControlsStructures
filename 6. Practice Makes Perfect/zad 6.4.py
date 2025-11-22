# Password validator
# New password is at least 12 characters long

new_password = input('Enter new password: ')

if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    print('Password is long enough')



#pobranie hasła
#sprawdzenie długości len(new_password)
#jeśli < 12 → komunikat o błędzie
#w przeciwnym razie → hasło zaakceptowane