# 4. While. For what?
Eerst stukjes code om te beginnen:

#### Een For-loop
```python
for x in range(5):
    print("Hello", x)
```
Indexen (in programmeertalen) beginnen altijd bij 0. Dus hier is het 0-1-2-3-4. 5 in het totaal.

#### Een While-loop
Deze loop blijft doorgaan tot de waarde false is.
```python
index = 0
herhalen = True
while herhalen:
    if index > 4:
        print("herhalen op false zetten -> while stoppen")
        herhalen = False
    index += 1
print("De index", index)
```
Dit is belangrijk om te snappen!

## Oefeningen 1 - I can hear your echooooooo
Vraag een woord op. Laat dat woord even veel uitschrijven als het woord lang is. Vb: Hoi. Hoi = 3 letters. Dus: Hoi Hoi Hoi.

*TIP: de lengte van een String kan je weten door `len(string1)`.*

## Oefeing 2 - Lower Lower Lower
Begin met `number = 5`. Zorg ervoor dat je het nummer blijft vragen tot wanneer het getal kleiner dan 0 is.

## Oefening 3 - Stop it now!
Ik wil de som hebben van alle getallen die ik ga invoeren totdat het woord "stop" is ingevoerd. Vb: 2 3 stop => 6

*TIP: een string vergelijken met andere kan met `string1 == string2` of `string1 != string2`. `!` betekent: NIET.*

## Oefening 4 - Schoonduiken v1
Wedstrijd schoonduiken. Bepaal de gemiddelde score voor de duikers.
##### Invoer
De eerste regel bevat een getal n∈N
(n≥3) dat aangeeft hoeveel juryleden er zijn. Daarna volgen n regels, met op elke regel de score s∈N toegekend door een jurylid.
##### Uitvoer
Eén enkele regel met daarop de finale score van de deelnemer.
##### Voorbeeld
###### invoer 
```python
4
100
0
55
56
```
###### uitvoer
```python
56
```