time_24 = input('Enter time (24-hour format): ')   # e.g. 16:32

# split into hours and minutes
hours_24, minutes = time_24.split(':')
hours_24 = int(hours_24)

# determine am/pm
if hours_24 == 0:
    hours_12 = 12
    suffix = 'am'
elif hours_24 < 12:
    hours_12 = hours_24
    suffix = 'am'
elif hours_24 == 12:
    hours_12 = 12
    suffix = 'pm'
else:
    hours_12 = hours_24 - 12
    suffix = 'pm'

print(f'Time in 12-hour format: {hours_12}:{minutes}{suffix}')



#rozdzielenie godzin i minut (split(':'))
#sprawdzenie zakresu godzin 24h
#konwersja do 12h przez odejmowanie 12
#wybór am/pm
#wypisanie wyniku w formacie 12h