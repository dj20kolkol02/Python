Zad2/lista2
import random
import csv
import os

# Funkcja do wczytywania losowych imion, nazwisk, ulic, miast i krajów z odpowiednich plików tekstowych.
def load_data_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        data = file.readlines()
    return [line.strip() for line in data]

# Funkcja do generowania unikalnych danych osobowych.
def generate_personal_data():
    first_names = load_data_from_file('imiona.txt')
    last_names = load_data_from_file('nazwiska.txt')
    streets = load_data_from_file('ulice.txt')
    cities = load_data_from_file('miasta.txt')
    countries = load_data_from_file('kraje.txt')

    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        pesel = ''.join([str(random.randint(0, 9)) for _ in range(11)])
        street = random.choice(streets)
        house_number = random.randint(1, 50)
        city = random.choice(cities)
        country = random.choice(countries)

        yield f"{first_name};{last_name};{pesel};{street};{house_number};{city};{country}"

# Funkcja do zapisywania danych do pliku CSV.
def save_to_csv(filename, num_records):
    with open(filename, 'w', encoding='utf-8') as file:
        unique_data = set()
        for data in generate_personal_data():
            if data not in unique_data:
                file.write(data + '\n')
                unique_data.add(data)
                num_records -= 1
            if num_records == 0:
                break

num_records = int(input("Podaj ilość rekordów do wygenerowania: "))
save_to_csv('dane_osobowe.csv', num_records)
print(f"Wygenerowano {num_records} unikalnych rekordów i zapisano je w pliku dane_osobowe.csv")

szukane = str(input('Podaj nazwisko ktore chcesz wyszukac: '))
with open('dane_osobowe.csv', encoding='utf-8', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=';')
    for row in csv_reader:
        if(str(szukane) == str(row[1])):
            print(f'Imie: {row[0]}\nNazwisko: {row[1]}\nPesel: {row[2]}\nUlica: {row[3]}\nNumer domu: {row[4]}\nMiasto: {row[5]}\nKraj: {row[6]}\n\n')