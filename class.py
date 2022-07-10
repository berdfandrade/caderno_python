class PartyAnimal():  # This is the template for making PartyAnimal objects
    x = 0  # Each PartyAnimal object has a bit of data.

    def party(self):  # a identaçãode 'def' fica dentro da classe.
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()        # construct a PartyAnimal object and store in an

an.party()
an.party()  # PartyAnimal.party(an)
an.party()
