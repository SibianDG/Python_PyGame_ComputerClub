aantalJuryLeden = int(input())
punten = []

for jurylid in range(aantalJuryLeden):
    punten.append(int(input()))
punten.sort()

minP = punten[0]
punten.remove(minP)
aantalJuryLeden -= 1

maxP = punten[len(punten)-1]
punten.remove(maxP)
aantalJuryLeden -= 1

som = 0
for punt in punten:
    som += punt
print(round(som/aantalJuryLeden))

