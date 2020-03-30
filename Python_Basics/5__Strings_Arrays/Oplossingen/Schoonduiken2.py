aantalJuryLeden = int(input())
punten = []

for jurylid in range(aantalJuryLeden):
    punten.append(int(input()))
#sorteer de lijst
punten.sort()

#de laagste score verwijderen
punten.remove(punten[0])

# hoogste score verwijderen andere manier
del punten[len(punten)-1]
# korter:
# del punten[-1] # -1 geeft de laatste index

# aantal juryleden verminderen met 2.
aantalJuryLeden -= 2

som = 0
for punt in punten:
    som += punt
print(round(som/aantalJuryLeden))

