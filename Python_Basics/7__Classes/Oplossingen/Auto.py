class Auto:
    def __init__(self, merk, model, kleur):
        self.merk = merk
        self.model = model
        self.kleur = kleur

    def zinvolleZin(self):
        print("Ik ben een", type(self).__name__.lower(), "van het merk", self.merk, "en model", self.model,
              "met als kleur", self.kleur)

tesla = Auto("Tesla", "Model 3", "wit")
tesla.zinvolleZin()