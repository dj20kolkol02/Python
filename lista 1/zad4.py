zdanie = str(input('Wpisz zdanie: '))
bez_spacji = []
bez_znaku = []
for i in range(len(zdanie)):
    if zdanie[i] == ' ':
        i += 1
    else:
        bez_spacji = bez_spacji + [zdanie[i]]
        i += 1

znak = input('Podaj znak, ktory chcesz pominac: ')
for i in range(len(zdanie)):
    if str(zdanie[i]) == str(znak):
        i += 1
    else:
        bez_znaku = bez_znaku + [zdanie[i]]
        i += 1

print(f'Dlugosc zdania: {len(zdanie)}')
print(f'Dlugosc zdania bez spacji: {len(bez_spacji)}')
print(f'Dlugosc zdania bez {znak}: {len(bez_znaku)} ')

print(f'Poczatkowe zdanie: \n{zdanie}')
print('Podzial w oparciu o spacje:')
bez_spacji = zdanie.split(" ")
for i in range(len(bez_spacji)):
    print(bez_spacji[i])

print(f'Podzial w oparciu o {znak}: ')
bez_znaku = zdanie.split(znak)
for i in range(len(bez_znaku)):
    print(bez_znaku[i])