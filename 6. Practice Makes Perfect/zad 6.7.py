age = int(input('Enter your age: '))

if age < 13:
    print('Child')
elif 13 <= age <= 19:
    print('Teen')
elif 20 <= age <= 64:
    print('Adult')
else:
    print('Senior')



#<13 → Child
#13–19 → Teen
#20–64 → Adult
#≥65 → Senior