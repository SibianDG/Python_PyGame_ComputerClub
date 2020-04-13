aantalStapels = int(input())
gewicht = int(input())
gewichtAlles = int(input())

print(abs(round((((aantalStapels * (aantalStapels + 1)) / 2) * gewicht - gewichtAlles))))
