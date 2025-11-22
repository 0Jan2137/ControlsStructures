print("SURVEY")

q1 = input("Are you interested in computer science? (y/n): ")
q2 = input("Do you like playing computer games? (y/n): ")
q3 = input("Do you have an Instagram account? (y/n): ")

# convert answers to logical (True/False)
interested_cs = (q1 == 'y')
playing_games = (q2 == 'y')
has_instagram = (q3 == 'y')

print("\nSURVEY RESULTS")
print("Interested in computer science:", "Yes" if interested_cs else "No")
print("Playing computer games:", "Yes" if playing_games else "No")
print("Has an Instagram account:", "Yes" if has_instagram else "No")



#pobranie odpowiedzi y/n
#zamiana na wartości logiczne True/False
#wypisanie wyników w formacie „Yes/No”