lista = [] 
# lista = [None] * 15
for i in range(0,15):
    lista.append(int(input(f'Podaj nazwe {i+1} elementu listy:')))
    # lista[i] = int(input(f'Podaj wartosc {i+1} elementu listy: '))

import modul1
lista_odp = [None] * 4
lista_odp = modul1.najmniejsza_i_najwieksza(lista)
print(f'Najmniejsza wartosc to {lista_odp[0]} na pozycji {lista_odp[1]}')
print(f'Najwieksza wartosc to {lista_odp[2]} na pozycji {lista_odp[3]}')

import modul2
sr = modul2.srednia(lista)
print(f'Srednia wartosc listy to {sr}')

wartosc = int(input('Podaj wartosc, aby odnalezc jej pozycje: '))
import modul3
poz = modul3.pozycja(lista,wartosc)
print(f'Wartosc {wartosc} znajduje sie na pozycji {poz}')


import modul4
med = modul4.mediana(lista)
print(f'Srodkowa wartosc, czyli mediana to {med}')