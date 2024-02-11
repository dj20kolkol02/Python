import pola
import gracz
import pickle

def stworzPola():
    listaPol=[]
    listaPol.append(pola.TPole("Start"))
    listaPol.append(pola.TPoleDoKupienia("Nysa",80))
    listaPol.append(pola.TPoleDoKupienia("Kluczbork",100))
    listaPol.append(pola.TPoleDoKupienia("Opole",120))
    listaPol.append(pola.TPolePodatek("Podatek"))
    listaPol.append(pola.TPoleKolej("Kolej 1",100))
    listaPol.append(pola.TPoleDoKupienia("Słupsk",130))
    listaPol.append(pola.TPoleDoKupienia("Malbork",180))
    listaPol.append(pola.TPoleWodociag("Sopot",100))
    listaPol.append(pola.TPoleDoKupienia("Gdynia",190))
    listaPol.append(pola.TPoleDoKupienia("Gdańsk",200))
    listaPol.append(pola.TPoleKolej("Kolej 2",100))
    listaPol.append(pola.TPoleDoKupienia("Dąbrowa Górnicza",210))
    listaPol.append(pola.TPoleDoKupienia("Zabrze",220))
    listaPol.append(pola.TPoleDoKupienia("Bytom",230))
    listaPol.append(pola.TPoleDoKupienia("Bielski-Biała",240))
    listaPol.append(pola.TPoleDoKupienia("Rybnik",250))
    listaPol.append(pola.TPoleDoKupienia("Sosnowiec",260))
    listaPol.append(pola.TPoleDoKupienia("Gliwice",270))
    listaPol.append(pola.TPoleDoKupienia("Katowice",280))
    listaPol.append(pola.TPoleKolej("Kolej 3",100))
    listaPol.append(pola.TPoleDoKupienia("",300))
    listaPol.append(pola.TPoleDoKupienia("",310))
    listaPol.append(pola.TPoleWodociag("Wodociąg 2",100))
    listaPol.append(pola.TPoleDoKupienia("Bydgoszcz",320))
    listaPol.append(pola.TPoleDoKupienia("Gniezno",330))
    listaPol.append(pola.TPoleDoKupienia("Ostrów Wielkopolski",340))
    listaPol.append(pola.TPoleDoKupienia("Poznań",350))
    listaPol.append(pola.TPoleDoKupienia("Łódź",360))
    listaPol.append(pola.TPoleKolej("Kolej 3",100))
    listaPol.append(pola.TPoleDoKupienia("Świnoujście",370))
    listaPol.append(pola.TPoleDoKupienia("Szczecin",380))
    listaPol.append(pola.TPolePodatek("Podatek"))
    listaPol.append(pola.TPoleDoKupienia("Warszawa",400))
    return listaPol

def stworzGraczy(ilosc):
    listaGraczy=[]
    if (ilosc<2 or ilosc>4):
        ilosc=4
    for el in range(ilosc):
        nazwa=input("Nazwa {} gracza: ".format(el+1))
        listaGraczy.append(gracz.TGracz(nazwa,1500))
    return listaGraczy

def funSprzedaz(gracz,listaPol,listaGraczy):
    while gracz.money<0:
        if len(gracz.posiadane)==0:
            print("Gracz {} zbankrutował".format(gracz.nazwa))
            for el in range(len(listaGraczy)):
                if listaGraczy[el].nazwa==gracz.nazwa:
                    del listaGraczy[el]
            if len(listaGraczy)==1:
                print("Gracz {} wygrał!".format(listaGraczy[0].nazwa))
                return False
            return True
        else:    
            print("Masz {} pieniędzy, musisz coś sprzedać".format(gracz.money))
            for el in range(len(gracz.posiadane)):
                print("{}. {} Cena: {}".format(el+1,listaPol[gracz.posiadane[el]].nazwa,listaPol[gracz.posiadane[el]].cenaZakupu))
            sprzedaz=int(input("Które pole sprzedać? "))-1
            listaPol[gracz.posiadane[sprzedaz]].wlasciciel="Nie"
            gracz.money+=listaPol[gracz.posiadane[sprzedaz]].cenaZakupu
            del gracz.posiadane[sprzedaz]
    return True

def funZapis(listaPol,listaGraczy):
    zapis=input("Pod jaką nazwą chcesz zapisać? ")+".dat"
    bazaZapis=[]
    bazaZapis.append(listaPol)
    bazaZapis.append(listaGraczy)
    with open(zapis,'wb') as plik:
        pickle.dump(bazaZapis,plik)

def funWczytaj():
    wczytaj=input("Jaka jest nazwa pliku ? ")+".dat"
    with open(wczytaj,'rb') as plik:
        bazaDanych=pickle.load(plik)
    return bazaDanych

def wyswietlNieruchomosci(gracz, listaPol):
    print("\nNieruchomości gracza {}:".format(gracz.nazwa))
    if len(gracz.posiadane) == 0:
        print("Gracz nie posiada żadnych nieruchomości.")
    else:
        for idx in gracz.posiadane:
            pole = listaPol[idx]
            print("- {} ({})".format(pole.nazwa, pole.__class__.__name__))
