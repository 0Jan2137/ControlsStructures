x = int(input('x = '))
y = int(input('y = '))

if x == 0 and y == 0:
    print(f'Point P({x},{y}) is at the origin (0,0)')
elif x == 0:
    print(f'Point P({x},{y}) is on the Y axis')
elif y == 0:
    print(f'Point P({x},{y}) is on the X axis')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
else:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')



#(0,0) → punkt w początku układu
#x=0 → oś Y
#y=0 → oś X
#x>0,y>0 → I ćwiartka
#x<0,y>0 → II ćwiartka
#x<0,y<0 → III ćwiartka
#x>0,y<0 → IV ćwiartka