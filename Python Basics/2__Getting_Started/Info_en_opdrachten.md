# 2. Getting Started
Per oefening gaan we een nieuw Python bestandje maken. Zo kan je het achteraf altijd nog eens bekijken.

## Oefening 1 - Computer + Club = ComputerClub
Laat het script ComputerClub uitschrijven door 2 woorden aan elkaar te voegen.
```python
print("ComputerClub")
```
Het bovenstaande is verboden.

- *TIP1: het zit in de titel*
- *TIP2: tekst in het algemeen wordt gezien als Strings in programmeertalen. Als je wil zeggen dat je een String/tekst wil printen (of opslaan of andere), gebruik dan dubble aanhalingstekens. Vb: "Hoi" == 'Hoi' (in Python is er geen verschil).*

## Oefening 2 - De vragenronde
Stukje code. Raad eens wat het doet:
```python
print("Wat is je naam?")
# een "#" voor de regels zorg ervoor dat deze lijn niet uitgevoerd wordt en is dus commentaar.
# voer je naam in in de console
naam = input()
print("Naar welke podcast luister je?")
# voer de podcast in
podcast = input()
print(f"Dag {naam}, jij luistert dus vaak naar {podcast}. Dat is leuk.")
print("Van die podcast "+ podcast + "heb ik nog niet gehoord.")
print('Fijn je ontmoet te hebben,', naam)
```
Je kan ook altijd een nieuwe file maken en het eens uitvoeren.

### Opdracht
Maak nu zelf een script waarbij je vraagt wie je bent en wanneer je jarig bent. Maak daarna een gepast zin met deze twee variabelen.

## Oefening 3 - 
Probeer een scriptje te maken waarbij je vraagt in welk jaar we zitten en hoe oud je bent. Laat dan in de console uitschrijven hoe oud je je dit jaar wordt of bent.

- *TIP1: als je gewoon min gebruikt zal het niet werken.*

- *TIP2: Als je via `input()` iets vraagt, dan is dat standaard een String of tekst. We moeten aan Python zeggen dat het een getal is. Getal in het Engels is Integer. Dus => `int( input() )`.*