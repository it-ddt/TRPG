import os

def show_location(user_name):
    is_on_arena = True

    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    while is_on_arena:

        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        user_choise = "0"
        while user_choise not in ("1", "2"):
            os.system("cls")
            print(f"{user_name} вошел на арену. Тут пока нечего делать.")
            print("----------")
            print("1 — Сражаться")
            print("2 — Вернуться в лагерь")
            user_choise = input("Что делать? ")

            # проверяем выбор игрока

            # сражаемся
            if user_choise == "1":
                print(f"Пока что {user_name} не может сражаться.")
                input("ENTER — дальше")
            
            # уходим в лагерь
            else:
                is_on_arena = False
                print(f"{user_name} отправился в лагерь.")
