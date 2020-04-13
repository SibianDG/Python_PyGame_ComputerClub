naam1 = input()
leeftijd1 = int(input())
naam2 = input()
leeftijd2 = int(input())

if leeftijd1 < leeftijd2:
    print(f"{naam1} is jonger dan {naam2}")
elif leeftijd1 > leeftijd2:
    print(f"{naam1} is ouder dan {naam2}")
else:
    print(f"{naam1} en {naam2} zijn even oud")