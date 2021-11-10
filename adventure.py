import os

def show_location(user_name):
    is_in_adventure = True

    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    while is_in_adventure:

        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        user_choise = "0"
        while user_choise not in ("1", "2"):
            os.system("cls")
            print(f"{user_name} выбрался из лагеря в окрестности. Тут пока нечего делать.")
            print("----------")
            print("1 — Поискать приключения")
            print("2 — Вернуться в лагерь")
            user_choise = input("Что делать? ")

            # проверяем выбор игрока

            # ищем приключения
            if user_choise == "1":
                print(f"Пока что {user_name} не сможет найти тут приключений.")
                input("ENTER — дальше")
            
            # уходим в лагерь
            else:
                is_in_adventure = False
                print(f"{user_name} отправился в лагерь.")
