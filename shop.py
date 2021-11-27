import os
import show_player


def show_location(user_name, user_money, user_hp, user_luck, user_inventory, game):
    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    is_busy = True
    potion_prise = 100
    while is_busy:
        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        os.system("cls")
        show_player.show(user_name, user_money, user_hp, user_luck, user_inventory, game)
        print(f"1 — Купить зелье за {potion_prise}")
        print("2 — Вернуться в лагерь")

        # игрок выбирает вариант
        user_choice = input("Что делать? ")

        # пытаемся купить зелье, денег хватает
        if user_choice == "1" and user_money >= potion_prise:
            user_money -= potion_prise
            user_inventory.append("зелье")
            print(f"{user_name} купил зелье.")

        # пытаемся купить зелье, денег не хватает
        elif user_choice == "1" and user_money < potion_prise:
            print(f"У {user_name} не хватает денег.")

        # уходим в лагерь
        elif user_choice == "2":
            is_busy = False
            print(f"{user_name} отправился в лагерь.")

        # все остальные варианты
        else:
            print("Такого варианта нет, попробуйте другой.")

        input("ENTER — дальше")

    # мы не возвращаем инвентарь, он изменяемый объект и изменяется прямо в этом модуле
    # деньги — неизменяемый объект, возвращаем их их функции и переопределяем в главном файле (заменяем старое значение новым)
    return user_money
