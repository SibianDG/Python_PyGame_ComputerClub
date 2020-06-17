class Auto:
    def __init__(self, merk: str, model: str, kleur: str, elektrisch: bool, aantalDeuren=5):
        self.merk = merk
        self.model = model
        self.kleur = kleur
        self.elektrisch = elektrisch
        self.aantalDeuren = aantalDeuren
        self.controleerOpAantalDeuren()

    def zinvolleZin(self):
        motor = "verbrandings-"
        if self.elektrisch:
            motor = "elektrisch"
        print("Ik ben een", type(self).__name__.lower(), "van het merk", self.merk, "en model", self.model,
              "met als kleur", self.kleur, ". Ik heb een", motor, "motor met", self.aantalDeuren, "deuren.")

    def controleerOpAantalDeuren(self):
        if not isinstance(self.aantalDeuren, int) or self.aantalDeuren < 1:
            raise ValueError("Aantal deuren moet een int zijn.")


tesla = Auto("Tesla", "Model 3", "wit", True)
tesla.zinvolleZin()

ferrari = Auto("Ferrari", "4", "rood", False, 3)
ferrari.zinvolleZin()

fout1 = Auto("Mini", "Heeft dit een model?", "zwart", "nee", 3)
fout2 = Auto("Dacia", "Duster", "Geel", False, "vijf")
