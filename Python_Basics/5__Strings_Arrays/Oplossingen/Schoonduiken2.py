aantalJuryLeden = int(input())
punten = []

for jurylid in range(aantalJuryLeden):
    punten.append(int(input()))
#sorteer de lijst
punten.sort()

#de laagste score
minP = punten[0]
#verwijderen (maar 1x wordt de laagste score verwijderd)
punten.remove(minP)
# -1 voor het gemiddelde
aantalJuryLeden -= 1

maxP = punten[len(punten)-1]
punten.remove(maxP)
aantalJuryLeden -= 1

som = 0
for punt in punten:
    som += punt
print(round(som/aantalJuryLeden))

