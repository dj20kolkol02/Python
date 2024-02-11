oceny = []
nazwa_przedmiotu = []
print('Program liczy srednia ze wszystkich ocen czastokwych lub z danego przedmiotu')
licznik = int(0)
while True:
    while True:
        ocena = float(input('Ocena: '))
        if ocena in {2, 2.5, 3, 3.5, 4, 4.5, 5}:
            oceny = oceny + [ocena]
            break
        else:
            print("Nie ma takiej oceny! - sprobuj jeszcze raz")
    nazwa_przedmiotu = nazwa_przedmiotu + [str(input('Nazwa przedmiotu: '))]
    licznik += 1
    czy_dalej = int(input('Przejdz do obliczania sredniej -> 0: '))
    if czy_dalej == 0:
        break

while True:
    print('srednia ze wszystkich ocen wybierz 1')
    print('srednia z wybranego przedmiotu wybierz 2')
    wybor = int(input('Co chcesz zrobic? '))
    if(wybor == 1):
        srednia = sum(oceny) / len(oceny)
        print(f'Srednia ze wszystkich ocen wynosi {srednia}')
    elif(wybor == 2):
        przedmiot = str(input('Wybierz przedmiot: '))
        ile = int(0)
        suma = []
        for i in range(licznik):
            if(str(przedmiot) == str(nazwa_przedmiotu[ile])):
                suma = suma + [oceny[ile]]
                ile += 1 
            else:
                ile += 1
        sredniaP = sum(suma)/len(suma)
        print(f'Srednia z {przedmiot} wynosi {sredniaP}')
    else:
        print('Nieprawidlowy wybor opcji!')
        break
    dalej = input('Wyjscie -> Wybierz 0: ')
    if(dalej == '0'):
        break