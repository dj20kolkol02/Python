import pola
import gracz
import random
import funkcje as f

wczytaj = int(input("1.Wczytaj plik z zapisaną grą 2.Nowa gra  "))
if wczytaj == 1:
    bazaDanych = f.funWczytaj()
    listaPol = bazaDanych[0]
    listaGraczy = bazaDanych[1]
else:
    listaPol = f.stworzPola()
    gracze = int(input("Ilość graczy (od 2 do 4): "))
    listaGraczy = f.stworzGraczy(gracze)

x = True
while x:
    for el in range(len(listaGraczy)):
        popPoz = listaGraczy[el].pozId
        print("\nTura gracza {}, ilość gotówki {}".format(listaGraczy[el].nazwa, listaGraczy[el].money))
        print("\nGracz {} rzuca kością...".format(listaGraczy[el].nazwa))
        rzut = listaGraczy[el].rzut()
        pozycja = listaGraczy[el].pozId
        if popPoz > pozycja:
            print("\nPrzechodzisz przez pole Start... Dostajesz 200")
            listaGraczy[el].money += 200
        print(listaPol[pozycja])
        listaPol[pozycja].funOplata(listaGraczy[el], listaPol, listaGraczy, rzut)
        
        

        if listaGraczy[el].money < 0:
            x = f.funSprzedaz(listaGraczy[el], listaPol, listaGraczy)

    

    if x:
        xx = int(input("1.Kolejna runda 2.Zapisz stan rozgrywki 3.Wyjście 4.Zapis i wyjście 5.Wyświetl pola graczy\n? "))
        if xx == 2:
            f.funZapis(listaPol, listaGraczy)
        elif xx == 3:
            x = False
        elif xx == 4:
            f.funZapis(listaPol, listaGraczy)
            x = False
        elif xx == 5:
            for el in range(len(listaGraczy)):
                f.wyswietlNieruchomosci(listaGraczy[el], listaPol)
        
        

      


            
