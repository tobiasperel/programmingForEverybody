class PartyAnimal:
    x = 0
    name = ""
    def _init_(self,z):
       self.name = z
       print(self.name,"contructed")

    def party(self):
        self.x = self.x + 5
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
