###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))


if month >= 10:
    quarter = 4
elif month <= 3:
    quarter = 1
elif month <= 10 and month >= 6:
    quarter = 3
elif month <= 6 and month >= 4:
    quarter = 2
print(f'Month {month} is in quarter {quarter}')