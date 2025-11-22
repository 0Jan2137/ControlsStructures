car_speed = int(input('Enter car speed: '))

speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
else:
    print('Car speed is OK')



#min = 40 km/h, max = 140 km/h
#jeśli prędkość <40 lub >140 → błąd
#w przeciwnym razie → prędkość poprawna