soort1 = input()
getal1 = input()
soort2 = input()
getal2 = input()
kleurz1 = 'schoppen'
kleurz2 = 'klaveren'
kleurr1 = 'harten'
kleurr2 = 'ruiten'
if getal2 == getal1:
    if (soort1 == kleurr1 and soort2 == kleurr2) or (soort1 == kleurr2 and soort2 == kleurr1):
        print(f'{soort1} {getal1} en {soort2} {getal2} zijn makkers')
    elif (soort1 == kleurz1 and soort2 == kleurz2) or (soort1 == kleurz2 and soort2 == kleurz1):
        print(f'{soort1} {getal1} en {soort2} {getal2} zijn makkers')
    else:
        print(f'{soort1} {getal1} en {soort2} {getal2} zijn geen makkers')
else:
    print(f'{soort1} {getal1} en {soort2} {getal2} zijn geen makkers')
