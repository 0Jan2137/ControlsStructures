products = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if products > 2:
    discounted = products - 2                      # items with discount
    amount = 2 * price + discounted * (price * 0.75)
else:
    amount = products * price

print(f'Amount to pay: {amount:.2f}')



#pierwsze 2 produkty → normalna cena
#każdy kolejny → 25% taniej (czyli ×0.75)
#obliczenie kosztu normalnych i przecenionych sztuk
#wypisanie kwoty końcowej