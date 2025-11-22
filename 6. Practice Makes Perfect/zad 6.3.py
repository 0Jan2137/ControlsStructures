# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house

light_switch1 = False   # False - switch off, True - switch on
light_switch2 = False

bulbs_on = 0

# switch 1 turns on 1 bulb
if light_switch1:
    bulbs_on += 1

# switch 2 turns on 2 bulbs
if light_switch2:
    bulbs_on += 2

print(f'Number of bulbs that are on: {bulbs_on}')



#light_switch1 → dodaje 1 żarówkę
#light_switch2 → dodaje 2 żarówki
#sumujemy w bulbs_on
#wypisujemy wynik