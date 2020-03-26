#declaratie
arr = []
#toevoegen
arr.append("hallo")
arr.append(123)
arr.append("ComputerClub")
arr.append("Het is ochtend voor mij")
arr.append("test")
print(len(arr))
print(arr.pop(len(arr)-1))# pop is een index verwijderen en terug geven, en dus hier printen.

# over elk element gaan in de lijst:
for index in range(len(arr)):
    print(f"Op plaats {index} staat er {arr[index]}.") # arr[plaats] geeft de inhoud op die index in de lijst.

# over elk element lopen zonder index
for element in arr:
    print(element)

# wat extra's
cijferArray = [4, 1, 10, 3]
cijferArray.reverse()
print("Cijfer array reverse:")
for element in cijferArray:
    print(element, sep='')
cijferArray.sort()
print("Cijfer array sort")
for element in cijferArray:
    print(element, sep='')

