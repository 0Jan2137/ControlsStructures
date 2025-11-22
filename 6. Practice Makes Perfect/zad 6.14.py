facebook = True
twitter = False
instagram = True

# check if at least two accounts are True
if (facebook + twitter + instagram) >= 2:
    print('You are a good influencer!')
else:
    print('You are not a good influencer')



#wartości True/False traktujemy jak 1/0
#sumujemy trzy konta
#jeśli suma ≥ 2 → dobra obecność w social media
#wypisanie odpowiedniego komunikatu