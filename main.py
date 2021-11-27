"""
TODO:
сделать персонажа словарем
вынести функцию выбора вариантов в отдельный модуль
придумать систему диалогов
сделать прокачку персонажа: набирем опыта, получаем очки с каждым уровнем и тратим их на повышение навыков
"""

import os  # для очистки экрана
import shop  # модуль продавца зелий
import gamble  # модуль игры в кости
import arena  # модуль битвы на арене
import adventure  # модуль поиска приключений
import show_player # модуль печатает все параметы игрока

# создаем персонажа
user_name = "Вася Питонов"
user_money = 200
user_hp = 100
user_luck = 1
user_inventory = ["меч", "щит", "конь"]

# главный цикл игры
# заканчивается с гибелью игрока или выходоми из игры
game = True
while game:
    # печатаем инфу о месте и игроке
    # предлагаем игроку выбор действий
    os.system("cls")
    show_player.show(user_name, user_money, user_hp, user_luck, user_inventory, game)
    print(f"{user_name} сидит у костра в лагере. Отсюда можно отправиться в разные места.")
    print("1 — Зайти в лавку к алхимику")
    print("2 — Сыграть с разбойниками в кости")
    print("3 — Побродить по окрестностям")
    print("4 — Сразиться на арене")
    print("5 — Выйти из игры")

    # игрок выбирает вариант
    user_choice = input("Что делать? ")

    # вариант: идем за зельями
    if user_choice == "1":
        result = shop.show_location(user_name, user_money, user_hp, user_luck, user_inventory, game)
        user_money = result

    # вариант: играем в кости
    elif user_choice == "2":
        result = gamble.show_location(user_name, user_money, user_hp, user_luck, user_inventory, game)
        user_money = result

    # вариант: ищем приключения
    elif user_choice == "3":
        adventure.show_location(user_name, user_money, user_hp, user_luck, user_inventory, game)

    # вариант: сражаемся на арене
    elif user_choice == "4":
        arena.show_location(user_name, user_money, user_hp, user_luck, user_inventory, game)

    # вариант: выходим из игры
    elif user_choice == "5":
        game = False

    # все остальные варианты
    else:
        print("Такого варианта нет, попробуйте другой.")
        input("ENTER — дальше")

print("Конец.")
