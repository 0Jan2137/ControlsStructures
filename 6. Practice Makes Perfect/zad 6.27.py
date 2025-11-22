i = 6
while i > -1:         # odpowiada for i in range(6, -1, -3)
    j = 1
    while j < 4:      # odpowiada for j in range(1, 4)
        print(f'{i + j}', end=' ')
        j += 1
    print()
    i -= 3



#i startuje od 6 i maleje co 3 (6, 3, 0)
#dla każdego i, j rośnie od 1 do 3
#wypisujemy i + j, co daje układ klawiatury
#zamieniono obie pętle for na while