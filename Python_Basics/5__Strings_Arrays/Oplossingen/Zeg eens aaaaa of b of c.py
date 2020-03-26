letterInput = input()
woord = input()
aantal = 0
for letter in woord:
    if letter == letterInput:
        aantal += 1
print(aantal)

# of korter:
print(woord.lower().count(letterInput))

