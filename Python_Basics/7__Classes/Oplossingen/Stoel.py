class Stoel:
    def __init__(self, materiaal, kleur):
        self.materiaal = materiaal
        self.kleur = kleur

    def watPrecies(self):
        print("Ik ben een object van de klasse", type(self).__name__,
              "en ik ben gemaakt van het materiaal", self.materiaal, "met als kleur", self.kleur)

stoel1 = Stoel("hout", "groen")
stoel1.watPrecies()

stoel2 = Stoel("metaal", "blauw")
stoel2.watPrecies()