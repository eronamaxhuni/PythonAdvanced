class Student:
    def __init__(self, emri, mosha, kursi,notaMesatare):
        self.emri = emri
        self.mosha = mosha
        self.kursi = kursi
        self._notaMesatare=notaMesatare #variabel private

    def Pershendetje(self):
        print(f"Pershendetje une jam {self.emri} dhe mesoj {self.kursi} ")

    def _tregonota(self):
        print("this is a protected method")

Erona =Student("Erona",20,"python",)
Erona.Pershendetje()
