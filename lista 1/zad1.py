print('1. Objetosc i pole powierzchni kuli')
print('2. Objetosc i pole powierzchni prostopdloscinu')
print('3. Objetosc i pole powierzchni stozk')
print('4. Objetosc i pole powierzchni stozka scietego')
wybor = int(input('Co chcesz policzyc? '))
Pole = float
Objetosc = float
if wybor == 1:
    r = float(input('Promien kuli: '))
    Pole = 4 * 3.14 * r**2
    Objetosc = 4 / 3 * 3.14 * r**3
    print('Pole kuli = ' + str(Pole))
    print('Objetosc kuli = ' + str(Objetosc))
elif wybor == 2:
    r = float(input('Promien stozka: '))
    l = float(input('Tworzaca stozka: '))
    Pole = 2 * 3.14 * r * l + 2 * 3.14 * r**2
    Objetosc = 3.14 * r**2 * l
    print(f'Pole stozka = {Pole:.2f} ')
    print(f'Objetosc stozka = {Objetosc:.2f}')
elif wybor == 3:
    a = float(input('Dlugosc krotszej podstawy: '))
    b = float(input('Dlugosc dluzszej podstwy: '))
    h = float(input('Wysokosc prostopdloscianu: '))
    Pole = 2 * (a * b + a * h + b * h)
    Objetosc = a * b * h
    print(f'Pole prostopadloscianu = {Pole:.2f}')
    print(f'Objetosc prostopadloscianu = {Objetosc:.2f}')
elif wybor == 4:
    r = float(input('Dlugosc gornej podstawy: '))
    R = float(input('Dlugosc dolenj podstawy: '))
    h = float(input('Wysokosc stozka: '))
    l = float(input('Tworzaca stozka: '))
    Pole = 3.14 * (R + r) * l + 3.14 * (R ** 2 + r ** 2)
    Objetosc = 1/3 * 3.14 * h * (r**2 + r * R + R**2)
    print(f'Pole stozka scietego: {Pole:.2f}')
    print(f'Objetosc stozka scietego: {Objetosc:.2f}')
else:
    print('Nie ma takiej opcji')