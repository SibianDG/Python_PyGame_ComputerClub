getal = int(input())
zin = ""

if getal % 3 == 0:
    zin += "fizz"
if getal % 5 == 0:
    if zin != "":
        zin += " buzz"
    else:
        zin += "buzz"
if zin == "":
    zin = getal

print(zin)