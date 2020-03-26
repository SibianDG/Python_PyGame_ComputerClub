# 5. Strings in detail
## Oefening 1 - Zeg eens aaaaa of b of c
Maak een for-lus die over elke letter gaat van een woord. Geef het aantal '[letter die gevraagd is]' terug van het woord. Vb: `a` `Abba` print `2`.
- *TIP: een for lus kan ook zo gebruik worden: `for letter in woord:` en doe dan iets met letter.

## Arrays
Een array is een lijst. In die lijst kan je alles bijhouden, in steken verwijderen etc. Visuele voorstelling array:

| index | inhoud | index | inhoud | ... | ... | index | inhoud |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0 | "Hallo" | 1 | 123 | ... | ... | n-1 OF lengte-1 | "test" |
In Python werkt dit zo:
```python
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
    print(element, end='')
    #sep = seperator. Standaard is da " " spatie.
cijferArray.sort()
print("Cijfer array sort")
for element in cijferArray:
    print(element, end='')
```
## Oefening 2 - Voeg maar toe!
Maak een scriptje waarbij je getallen vraagt, die in een array steekt tot wanneer je het woord "stop" hebt getyped. Sorteer op het einde de lijst van groot naar klein. Overloop de lijst en print elke index + " : " + element af en gescheiden door een komma.
##### output:
`0 : 10, 1 : 5, 2 : 3,  3 : 2,  4 : 1`
*TIP: probeer op het einde geen komma te printen ;)*

## Oefening 3 - Veni Vidi Vici
Julius Caesar encrypteerde zijn brieven naar zijn leger om zo te voorkomen dat mocht het onderschept worden, dat niemand het zou kunnen lezen zonder de juist "key".
Maak een encryteer script dat alle letters met vervangt door key-aantal letters erna. Rekening houdend dat het een circulair alfabet is en na de Z komt weer de A.

*TIP: gebruik Strings of Arrays, modulo, invoer en vergelijkingen.*
*TIP2: String werken ook als arrays. Je kan `woord[index]` nemen.*
*TIP3: Als je wil weten of iets in een String of array zit gebruik dan `in -> letter in woord?`*

Een beetje zoeken kan geen kwaad. 

## Oefening 4 - Yhql Ylgl Ylfl
Ik ben een generaal en ik wil de code ontcijferen van Julius Caesar. De key is 3 en de zin is "Yhql Ylgl Ylfl". Wat was de originele zin?
