class Vertebrtes:
    def __init__(self, backBone =True ):#backbone is true by default
        self.has_backBone=backBone
    def vertebrate_info(self):
        print(f"vertebrates have a backbone")

class Aquatic:
    def __init__(self, habitat ="water"):
        self.habitat=habitat
    def aquatic_info(self):
        print(f'aquatic animals live in water')

class Fish(Vertebrtes, Aquatic):
    def __init__(self, species, backbone=True, habitat="water"):
        super().__init__(backBone=backBone)
        self.habitat=habitat
        self.species=species

    def fish_info(self):
        print(f"the {self.species} is a type of fish found in {self.habitat}")

    def swim(self):
        print(f"the fish is swimming")

goldFish = Fish("golden fish")
print(goldFish.has_backBone)
goldFish.swim()
