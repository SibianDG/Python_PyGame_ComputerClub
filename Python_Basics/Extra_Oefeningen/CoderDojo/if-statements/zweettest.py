aantalMaanden = int(input())
waarde = int(input())

if aantalMaanden <= 6:
    if waarde <= 29:
        print("CF is hoogst onwaarschijnlijk")
    elif waarde <= 59:
        print("CF is mogelijk")
    else:
        print("CF is waarschijnlijk")
else:
    if waarde <= 39:
        print("CF is hoogst onwaarschijnlijk")
    elif waarde <= 59:
        print("CF is mogelijk")
    else:
        print("CF is waarschijnlijk")

