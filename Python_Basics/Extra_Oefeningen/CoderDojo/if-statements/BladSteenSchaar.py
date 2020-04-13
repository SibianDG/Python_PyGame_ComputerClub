speler1 = input().lower()
speler2 = input().lower()

if speler1 == speler2:
    print("gelijkspel")
elif speler1 == "blad":
    if speler2 == "steen":
        print("speler1 wint")
    else:
        print("speler2 wint")
elif speler1 == "steen":
    if speler2 == "schaar":
        print("speler1 wint")
    else:
        print("speler2 wint")
elif speler1 == "schaar":
    if speler2 == "blad":
        print("speler1 wint")
    else:
        print("speler2 wint")
