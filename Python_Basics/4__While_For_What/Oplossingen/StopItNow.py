print("Geef nummer")
nummer = input()
som = 0

while nummer != "stop":
    som += int(nummer)
    print("Geef nummer")
    nummer = input()

print(f"Het product van alle getallen is {som}.")

