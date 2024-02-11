import random

class TGracz:
    def __init__(self,nazwa,money):
        self.nazwa=nazwa
        self.money=money
        self.pozId=0
        self.posiadane=[]
    def rzut(self):
        rzut=random.randrange(1,12)
        print("Wyrzuciles ",rzut)
        self.pozId+=rzut
        if self.pozId>39:
            self.pozId-=40
        return rzut
