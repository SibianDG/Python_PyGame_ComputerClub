# 7. Classes

### Wat is een class of een klasse

##### Wikipedia
[Een klasse in de zin van de objectoriëntatie is een mechanisme dat in bepaalde, objectgeoriënteerde programmeertalen gebruikt wordt om de toestandsruimte en interface van een verzameling objecten vast te leggen. Een klasse wordt ook wel omschreven als een sjabloon voor objecten.](https://nl.wikipedia.org/wiki/Klasse_(informatica))

##### Verduidelijking:
Je bent een fabriek. Je wil soorten stoelen maken, allemaal personaliseerd. We kunnen de fabriek voorstellen als een klasse. Je wil een stoel van vb. hout in kleur groen. Je wil een andere stoel van staal in het kleur blauw. ALs je de basis hebt, de klasse, dan kan je elke stoel maken die je wil door een nieuw object aan te maken van de klasse stoel. Stoel1 is dan een instantie van de klasse stoel. Maar hoe weet de de fabriek of de klasse nu hoe de stoel gemaakt moet worden? Bij het aanmaken van het object roep je de constructor op. Dat is een soort contract hoe de stoel er moet uitzien. Dus je schrijft op je contract of in de contructor welke parameters het object moet hebben.

Hoe ziet dat er dan precies uit in Python? Probeer onderstaande code eens uit te voeren. [De file vind je hier](./Oplossingen/Stoel.py).

```python
class Stoel:
    # def staat voor een aanroepbare functie.
    def __init__(self, materiaal, kleur): # hier is de functie de constructor. Het contract hoe een object eruit ziet is in Python __init__(self, ...paramters) 
        self.materiaal = materiaal
        self.kleur = kleur

    def watPrecies(self): # bij een functie geef je jezelf altijd mee. Dit is zo in Python. Gewoon te kennen ;)
        print("Ik ben een object van de klasse", type(self).__name__,
              "en ik ben gemaakt van het materiaal", self.materiaal, "met als kleur", self.kleur)

stoel1 = Stoel("hout", "groen")
stoel1.watPrecies()

stoel2 = Stoel("metaal", "blauw")
stoel2.watPrecies()
```

### Oefening 1
- Maak een klasse Auto. De parameters zijn: merk, model en kleur.
- Maak een functie die alle paramaters in een zinvolle tekst zet.

Een mogelijke oplossing vind je [hier](./Oplossingen/Auto.py)

### Oefening 2
- Neem de basis van oefening 1
- Zorg ervoor dat merk, model en kleur strings zijn.
- Voeg de volgende paramters toe: elektrisch (boolean) en aantal deuren (int)
- Als het aantal deuren niet is meegegeven bij de constructor, dan zet je het aantal deuren automatisch op 5. 5 is dan de defaultwaarde of de standaardwaarde.
    - Zoek eens op het internet naar "Defaultvalue Python", want programmeren is ook veel online opzoeken.
- Zorg ervoor dat de `aantalDeuren` van het type int is én minstens 1 deur bevat.
    - Als dit niet het geval is, dan werp je een Exception op of een fout.
    - `raise TypeError("Parameter moet een boolean zijn.")`

Een mogelijke oplossing vind je [hier](./Oplossingen/Auto2.py)

### Oefening 3
- Neem de basis van oefening 1
- Maak een dictionay met daarin de key als merk en de value de prijsklasse. Vb: Ferrari -> Duur. Renault -> Goedkoop. BMW -> Redelijk duur etc.
- Na het aanmaken van het object vraag je in welke prijsklasse dat merk zit.

Een mogelijke oplossing vind je [hier](./Oplossingen/Auto3.py)



