aantalJuryLeden = int(input())
gemiddelde = 0
for jurylid in range(aantalJuryLeden):
    punten = int(input())
    if punten >= 0:
        gemiddelde += punten
print(round(gemiddelde/aantalJuryLeden))

