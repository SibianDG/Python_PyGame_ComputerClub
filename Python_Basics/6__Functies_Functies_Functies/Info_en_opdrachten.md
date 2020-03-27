# 6. Functies, Functies en nog meer functies
#### belangrijk om te kunnen en snappen!

Vooraleer we beginnen moeten we 2 dingen leren: Functies en automatische testen.
### Functies
functies worden aangeroepen om duplicatie van code te vermijden. Hetzelfde verschillende keren opnieuw aan te roepen. Voorbeeld:
```python
def zegEensHallo(aantalKeer):
    for _ in range(aantalKeer):  # _ betekent dat je de variabele niet gebruikt.
        print("Hallo")


def watIsJeNaam():
    print("Wat is je naam")
    return input()  # return geeft een waarde terug waar de functie is opgeroepen


def zegEensHalloMetNaam(naam, aantalKeer):
    for index in range(aantalKeer):
        if index == 0:
            print("Dag", naam)
        else:
            print("Hallo")


zegEensHallo(5)
naam = watIsJeNaam()
zegEensHalloMetNaam(naam, 5)
# zegEensHalloMetNaam(watIsJeNaam(), 5)
```

## Oefening 1 - Scrabble
Begin met de volgende code. Alles tussen """ zijn de testen. Dit is handig om te controleren of je juist bent zonder naar de oplossing te kijken. Je moet dan ook vanonder dat hebben zoals in de code hieronder. Die __ __main__ __ voert de testen uit. Als je het programma wilt uitvoeren zonder testen, laat dan de laatste 3 lijnen weg en roep de functie aan. *Als de testen niet werken dan kan je altijd de laatste 3 lijnen verwijderen en zelf testen invoeren enventueel m.b.v. de testen in de opgaves.*
```python
import imp

def woordWaarde(woord):
    """
    >>> woordWaarde('Hello')
    12
    >>> woordWaarde('ComputerClub')
    36
    """
#hier de code
def letterWaarde(letter):
    """
    >>> letterWaarde('a')
    1
    >>> letterWaarde('Q')
    10
    """
    # punten is een dictionary. Voor elke eerste "key" heeft dat een value. key "a" heeft als waarde 1 enz. Werkt als een array, dus gebruik het als een array :] 
    punten = {"a": 1, "b": 3, "c": 5, "d": 2, "e": 1, "f": 4, "g": 3, "h": 4, "i": 1, "j": 4, "k": 3, "l": 3, "m": 3,
              "n": 1, "o": 1, "p": 3, "q": 10, "r": 2, "s": 2, "t": 2, "u": 4, "v": 4, "w": 5, "x": 8, "y": 8, "z": 4}
    # maak van de letter een kleine letter en geef de overeenkomstige waarde 

if __name__ == '__main__':
    import doctest
    doctest.testmod()

```

## Oefening 2 - Maak gebruikersnaam
Om te kunnen inloggen heb je een gebruikersnaam en een wachtwoord nodig. Een gebruikersnaam bestaat enkel uit kleine letters, en wordt samengesteld uit de eerste letter van je voornaam en de letters van je familienaam.

Bepaal de gebruikersnaam van een persoon. Hiervoor ga je als volgt te werk:
- Schrijf een functie eerste_letter waaraan een naam (str(ing)) moet doorgegeven worden. De functie moet de eerste letter (str) van de naam teruggeven.
- Schrijf een functie gebruikersnaam waaraan de voornaam (str) en de familienaam (str) van een persoon moeten doorgegeven worden. De functie moet de gebruikersnaam (str) van de persoon teruggeven.

```python
import imp

def eerste_letter(naam):

    """
    >>> eerste_letter('Sansa')
    'S'
    >>> eerste_letter('Jon')
    'J'
    """

def gebruikersnaam(voornaam, familienaam):

    """
    >>> gebruikersnaam('Sansa', 'Stark')
    'sstark'
    >>> gebruikersnaam('Jon', 'Snow')
    'jsnow'
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

## Oefening 3 - Nokia, where are you at?
<img src="./nokia.jpg" alt="Nokia phone">
Maak een script dat 1. Vraagt welke woord je wil typen. 2. Dat toont op welke cijfers je moet klikken.
Vb:

- `input` : `hoi`
- `output` : `44 666 444`

Begin met het volgende:

__TODO testen__

```python
import imp

def vraagWoord():
#code hieronder
    
def nokiaTypen(woord):
    """
    >>> nokiaTypen('hoi')
    '44 666 444 '
    >>> nokiaTypen('Jon')
    '222 666 6 7 88 8 33 777 222 555 88 22 '
    """
#code hieronder

def toetsen(letter):
    """
    >>> nokiaTypen('a')
    2
    >>> nokiaTypen('z')
    9999
    """
#code hieronder

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

## Oefening 4 - OXO
Het maken van games heeft vaak 2 fasen.
1. Het domein maken, of beter gezegd de achterliggende code zoals we al 6 reeksen doen.
2. De lay-out maken en de code verbinden met de lay-out.

*Opmerking: je kan ze ook combineren.*

#### Extra info: 2 dimensionale arrays.
Een speelveld is vaak een x-y rooster. Bij OXO is dat dan 3x3. Dat kan je makkelijk voorstellen in een 2 dimensionale array. Je hebt 3 rijen en 3 kolommen.
```python
array = ["x", "o", "x"] # is 1 rij.
array2 = [["x", "o", "x"], ["x", "x", "x"], ["x", "o", "x"]] #is een 2 dimensionale array.
# ik wil teken in het midden. rijen 0 - 1 - 2 => 1; kolommen 0 - 1 - 2 => 1
print(array2[1][1]) # dat element uitprinten.
# spelbord uitprinten:
for rij in array2:
    # rij is een array: ["x", "o", "x"]
    for kolom in rij:
        print(kolom, end='')
    print("\n") #print new line
# x o x
# x x x
# x o x
``` 
#### opdracht: Maak TicTacToe
Maak TicTacToe met een speelveld van 3x3. De eerste die OXO vormt is gewonnen.
Voor degene die eens alles zelf willen proberen. Ga je gang! *Gebruik wel functies, want we zitten in dit hoofdstuk ;)*

Voor degene die nog een beetje twijfelen. Kijk in de map "Oefeningen", daar heb ik al een start gezet.
Veel succes!