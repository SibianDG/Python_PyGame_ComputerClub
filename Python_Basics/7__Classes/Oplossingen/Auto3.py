class Auto:
    def __init__(self, merk, model, kleur):
        self.merk = merk
        self.model = model
        self.kleur = kleur

    def zinvolleZin(self):
        print("Ik ben een", type(self).__name__.lower(), "van het merk", self.merk, "en model", self.model,
              "met als kleur", self.kleur)

    def prijsKlasse(self):
        dictAutoPrijsklasse = {"Ferrari": "duur", "Renault": "goedkoop", "BMW": "redelijk duur", "Tesla": "Voorlopig nog duur", "McClaren": "duur"}

        if self.merk in dictAutoPrijsklasse:
            print(dictAutoPrijsklasse.get(self.merk))


tesla = Auto("Tesla", "Model 3", "wit")
tesla.prijsKlasse()