"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.
    1. При запуске, программа спрашивает имя игрока.
    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру
    3. При выходе из программы данные игрока записывать в файл (txt либо json).
    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.
"""
from random import randint
import json

def main():
    games = 0
    record = 0
    attempts = 0
    avg_attempts = 0
    magic(games, record, attempts, avg_attempts)


def magic(games, record, attempts, avg_attempts):
    name = input("Введите имя: ")
    a = int(input("Начало отрезка: "))
    b = int(input("Конец отрезка: "))
    max_try = b - a
    record = max_try
    while True:
        number = int(input("Введите число: " ))
        if number >= a and number <= b:
            rand = randint(a, b)
            count = 1
            while number != rand:
                if number > rand:
                    print('Введенное число больше сгенерированного')
                elif number < rand:
                    print('Введенное число меньше сгенерированного')
                number = int(input("Введите число: "))
                count += 1
            else:
                print("Число: ", number)
                print("Количество попыток: ", count)
                if count < record:
                    print("Новый рекорд: ", record)
                    record = count
                else:
                    print("Твой рекорд не изменился: ", record)
                games += 1
                attempts += count
                count = 0
                avg_attempts = attempts / games
                player_data(name, games, record, avg_attempts)
                if input("Continue? (Y/n) ") == "n":
                    print("Bye!")
                    break
        else:
            print("Введите число в пределах отрезка")


def player_data(name, games, record, avg_attempts):
    player_data = {
        "Name: " : name,
        "Games: " : games,
        "Record: " : record,
        "Avg_attempts: " : avg_attempts,
    }

    print(
        f"Имя: {name}\n",
        f"Количество игр: {games}\n",
        f"Рекорд: {record}\n",
        f"Cреднее количество попыток за игру: {avg_attempts}"
    )

    with open("Player_data.json", "a") as f:
        data = json.dumps(player_data, indent = 4)
        f.write(data)


if __name__ == "__main__":
    main()