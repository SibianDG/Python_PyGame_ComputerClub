print("In welk jaar leven we?")
huidigJaar = int(input())  # standaard waarde van input() is String. Om te kunnen rekenen moet jet het omzetten in een
# int met int().
print("In welk jaar ben je geboren?")
geboorteJaar = int(input())
print(f"Dus jij wordt of jij bent dit jaar {huidigJaar - geboorteJaar}.")
