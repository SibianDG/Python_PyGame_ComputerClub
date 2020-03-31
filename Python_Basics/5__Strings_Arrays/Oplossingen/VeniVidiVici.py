alfabetGroot = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabetKlein = "abcdefghijklmnopqrstuvwxyz"
print("geef een zin in.")
zin = input()
print("geef de key. (Bij Julius Caesar was dat 3)")
key = int(input())
encrypted = ""
for teken in zin:
    if teken in alfabetKlein:
        indexAlfabet = alfabetKlein.index(teken)
        encrypted += alfabetKlein[(indexAlfabet + key) % 26]
    elif teken in alfabetGroot:
        indexAlfabet = alfabetGroot.index(teken)
        encrypted += alfabetGroot[(indexAlfabet + key) % 26]
    else:
        encrypted += teken
print(encrypted)
