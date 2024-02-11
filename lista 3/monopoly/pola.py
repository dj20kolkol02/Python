import random
import gracz

class TPole:
    nazwa="dodane pole"
    def __init__(self,nazwa):
        self.nazwa=nazwa
    def __str__(self):
        return "\nStoisz na polu {}".format(self.nazwa)
    def funOplata(*args):
        return "Pole bez oplat"

class TPolePodatek(TPole):
    def __init__(self,nazwa):
        self.oplata=200
        super().__init__(nazwa)
    def __str__(self):
        return super().__str__()+"\nOpłata: {}".format(self.oplata)
    def funOplata(self,gracz,*args):
        gracz.money-=200
        return "\nZaplaciłeś 200 podatku"

class TPoleDoKupienia(TPole):
    domki=0
    def __init__(self,nazwa,cenaZakupu,*args):
        self.cenaZakupu=cenaZakupu
        self.wlasciciel="Nie"
        self.oplata=cenaZakupu/2
        if (len(args)>0):
            self.oplata=args[0]
        super().__init__(nazwa)
    def __str__(self):
        if self.wlasciciel=="Nie":
            return super().__str__()+"\nCena Zakupu: {}".format(self.cenaZakupu)
        else:
            return super().__str__()+"\nWłaścicel: {}\nOpłata: {}".format(self.wlasciciel,self.oplata)
    def funOplata(self,gracz,listaPol,listaGraczy,*args):
        pozycja=gracz.pozId
        if listaPol[pozycja].wlasciciel=="Nie":
            kupno=int(input("Kupić pole?\n1.Tak\n2.Nie\n? "))
            if kupno==1:
                listaPol[pozycja].wlasciciel=gracz.nazwa
                gracz.money-=listaPol[pozycja].cenaZakupu
                gracz.posiadane.append(pozycja)
            if listaPol[pozycja].wlasciciel==gracz.nazwa:
                print("Pole należy do ciebie")
                kupno=int(input("Kupić domki?\n1.Tak\n2.Nie\n? >"))
                if kupno==1:
                    domki=listaPol[pozycja].domki
                    print("Aktualnie posiadasz {}\nJeden domek kosztuje 100\nMożesz kupić {}".format(domki,5-domki))
                    ilosc=int(input("Ile chcesz kupić? "))
                    listaPol[pozycja].domki+=ilosc
                    listaPol[pozycja].oplata=(listaPol[pozycja].cenaZakupu/2)*(2*domki)
                    gracz.money-=100*ilosc
                    print("Masz teraz {} domkow na polu {}".format(listaPol[pozycja].domki,listaPol[pozycja].nazwa))
                
        elif listaPol[pozycja].wlasciciel==gracz.nazwa:
                print("Pole należy do ciebie")
                kupno=int(input("Kupić domki?\n1.Tak\n2.Nie\n? >"))
                if kupno==1:
                    domki=listaPol[pozycja].domki
                    print("Aktualnie posiadasz {}\nJeden domek kosztuje 100\nMożesz kupić {}".format(domki,5-domki))
                    ilosc=int(input("Ile chcesz kupić? "))
                    listaPol[pozycja].domki+=ilosc
                    listaPol[pozycja].oplata=(listaPol[pozycja].cenaZakupu/2)*(2*domki)
                    gracz.money-=100*ilosc
                    print("Masz teraz {} domkow na polu {}".format(listaPol[pozycja].domki,listaPol[pozycja].nazwa))
        else:
            for el in listaGraczy:
                if el.nazwa==listaPol[pozycja].wlasciciel:
                    el.money+=listaPol[pozycja].oplata
                    gracz.money-=listaPol[pozycja].oplata
                    print("Płacisz {} graczowi {}".format(listaPol[pozycja].oplata,el.nazwa))


class TPoleKolej(TPoleDoKupienia):
    def __init__(self,nazwa,cenaZakupu):
        self.oplata=cenaZakupu*2
        super().__init__(nazwa,cenaZakupu,self.oplata)
    def funOplata(self,gracz,listaPol,listaGraczy,*args):
        if listaPol[gracz.pozId].wlasciciel=="Nie":
            kupno=int(input("Kupić pole?\n1.Tak\n2.Nie\n? "))
            if kupno==1:
                listaPol[gracz.pozId].wlasciciel=gracz.nazwa
                gracz.money-=listaPol[gracz.pozId].cenaZakupu
                gracz.posiadane.append(gracz.pozId)
                print("Pole należy do ciebie")

                
        elif listaPol[gracz.pozId].wlasciciel==gracz.nazwa:
                print("Pole należy do ciebie")

        else:
            for el in listaGraczy:
                if el.nazwa==listaPol[gracz.pozId].wlasciciel:
                    el.money+=listaPol[gracz.pozId].oplata
                    gracz.money-=listaPol[gracz.pozId].oplata
                    print("Płacisz {} graczowi {}".format(listaPol[gracz.pozId].oplata,el.nazwa))

class TPoleWodociag(TPoleDoKupienia):
    def __init__(self,nazwa,cenaZakupu):
        super().__init__(nazwa,cenaZakupu)
    def __str__(self):
        if self.wlasciciel=="Nie":
            return super().__str__()+"\nCena Zakupu: {}".format(self.cenaZakupu)
        else:
            return super().__str__()+"\nWłaścicel: {}".format(self.wlasciciel)
    def funOplata(self,gracz,listaPol,listaGraczy,rzut):
        if listaPol[gracz.pozId].wlasciciel=="Nie":
            kupno=int(input("Kupić pole?\n1.Tak\n2.Nie\n? "))
            if kupno==1:
                listaPol[gracz.pozId].wlasciciel=gracz.nazwa
                gracz.money-=listaPol[gracz.pozId].cenaZakupu
                gracz.posiadane.append(gracz.pozId)
                print("Pole należy do ciebie")

                
        elif listaPol[gracz.pozId].wlasciciel==gracz.nazwa:
                print("Pole należy do ciebie")

        else:
            for el in listaGraczy:
                if el.nazwa==listaPol[gracz.pozId].wlasciciel:
                    oplata=10*rzut
                    el.money+=oplata
                    gracz.money-=oplata
                    print("Płacisz {} graczowi {}".format(oplata,el.nazwa))




