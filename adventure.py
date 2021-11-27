import os
import show_player


def show_location(user_name, user_money, user_hp, user_luck, user_inventory, game):
    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    is_busy = True
    while is_busy:
        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        os.system("cls")
        show_player.show(user_name, user_money, user_hp, user_luck, user_inventory, game)
        print(f"{user_name} выбрался из лагеря в окрестности. Тут пока нечего делать.")
        print("1 — Поискать приключения")
        print("2 — Вернуться в лагерь")

        # игрок выбирает вариант
        user_choice = input("Что делать? ")

        # вариант: ищем приключения
        if user_choice == "1":
            print(f"Пока что {user_name} не сможет найти тут приключений.")

        # вариант: уходим в лагерь
        elif user_choice == "2":
            is_busy = False
            print(f"{user_name} отправился в лагерь.")

        # все остальные варианты
        else:
            print("Такого варианта нет, попробуйте другой.")

        input("ENTER — дальше")
