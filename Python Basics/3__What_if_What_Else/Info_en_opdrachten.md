# 3. What If, What Else?
nieuw stukje code. Raad wat het doet:
```python
computerclubAflevering = 86
if computerclubAflevering < 52:
    print("ComputerClub bestaat nog geen jaar.")
elif computerclubAflevering < 52*2:
    print("ComputerClub is 1 jaar.")
else:
    print("Computerclub bestaan al meer dan 1 jaar.")
```
Je kan het altijd proberen uit te voeren of de waarden veranderen.

## Oefening 1 - Oei, wat is mijn BMI?
Vraag je lengte en gewicht. Bereken het BMI en geef een gepaste boodschap.

< 18 = ondergewicht; 18 - 25 = normaal gewicht; 25 - 27 = licht overgewicht; 27 - 30 = matig overgewicht; 30 - 40 = ernstig overgewicht; > 40 = ziekelijk overgewicht.

- *TIP1: formule BMI = gewicht delen door je lengte in meter in het kwadraat*
- *TIP2: werk met een variable `interpretatie = ''`. ALS het die waarde in, dan vul je die in, anders ...*

## Oefening 2 - ISBN controleren
ISBN. Dat zijn de cijfers aan de barcode van een boek (voor 1990 ongeveer. Meer info: Wikipedia).
ISBN bestaat uit 10 cijfers. 9 variabelen, 1 controle cijfer.
Opdracht: geef mij het laatste cijfer, controle cijfer als je de eerste 9 invult.

*TIP: het controle cijfer wordt berekent door de de plaats van het getal te vermenigvuldigen met het getal, alle 9 cijfers zo bij elkaar op te tellen en dan rest bij delen door 11.*
*TIP2: Hunk? M.a.w.( 1*getal1 + 2*getal2 + ... + 9*getal9) % 11 (modulo == % == rest na deling)
beetje zoeken kan geen kwaad hé ;)

## Oefening 3: Is het gelijk? Tel dan maar op
Korte oefening. Begin met de volgende code:
```python
index = 0
string1 = "Computer"
string2 = "computer"
string3 = "Computer"
```
Vergelijk elke variable met elkaar. Als het gelijk is, dan tel je bij de huidige index eentje bij op.
Print op het einde de index. (Het moet 1 worden ;) ) 

## Oefening 4: Maak zelf een oefening!
Vb: maak blad-steen-schaar. Het meeste leer je als je zelf fouten maakt en als je zelf oefeningen opstelt en maakt.

Weet je zelf een oefening? Maak een Pull request of stuur het door via Facebook of sibian@sibiandg.be !