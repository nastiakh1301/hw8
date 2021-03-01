"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.
    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""

data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}

def main():
    city = input("Input city: ")
    get_country(city)
    groupping_data(data)


def get_country(city):
    for i in data["Ukraine"]:
        if i == city:
            print("Ukraine")
    for i in data["France"]:
        if i == city:
            print("France")
    for i in data["Austria"]:
        if i == city:
            print("Austria")
    for i in data["Germany"]:
        if i == city:
            print("Germany")
    return True

def groupping_data(data):
    new_data = {}
    country = []
    city = []
    capital = []
    for i in data.keys():
        country == country.append(i)
    for i in data.values():
        capital == capital.append(i[0])
        i.pop(0)
        city == city.append(i)
    new_data["Country"] = country
    new_data["Capital"] = capital
    new_data["City"] = city
    print(new_data)
    return new_data


if __name__ == "__main__":
    main()