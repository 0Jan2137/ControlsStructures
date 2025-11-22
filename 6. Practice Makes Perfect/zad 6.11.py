current_price = float(input('Current product price: '))
previous_price = float(input('Previous product price: '))

price_drop = previous_price - current_price
percentage_drop = (price_drop / previous_price) * 100

if percentage_drop >= 10:
    print('Buy the product!!')

print(f'Product price reduced by {int(percentage_drop)}%')



#obliczenie różnicy cen
#wyliczenie procentowej zniżki
#jeśli spadek ≥ 10% → rekomendacja zakupu
#wypisanie procentu obniżki