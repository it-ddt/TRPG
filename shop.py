import os

def show_location(user_name, user_money, user_inventory):
    is_in_shop = True
    potion_prise = 100

    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    while is_in_shop:

        # печатаем инфу о месте и игроке
        # предлагаем игроку выбор действий
        user_choise = "0"
        while user_choise not in ("1", "2"):
            os.system("cls")
            print(f"{user_name} зашел в лавку алхимика. Тут уютно, но странно пахнет.")
            print(f"деньги: {user_money}")
            print(f"инвентарь:")
            for item in user_inventory:
                print("•", item)
            print("----------")
            print(f"1 — Купить зелье за {potion_prise}")
            print("2 — Вернуться в лагерь")
            user_choise = input("Что делать? ")

        # проверяем выбор игрока

        # пытаемся купить зелье, денег хватает
        if user_choise == "1" and user_money >= potion_prise:
            user_money -= potion_prise
            user_inventory.append("зелье")
            print(f"{user_name} купил зелье.")
            input("ENTER — дальше")

        # пытаемся купить зелье, денег не хватает
        elif user_choise == "1" and user_money < potion_prise:
            print(f"У {user_name} не хватает денег.")
            input("ENTER — дальше")

        # уходим в лагерь
        else:
            is_in_shop = False
            print(f"{user_name} отправился в лагерь.")

    # мы не возвращаем инвентарь, он изменяемый объект и изменяется прямо в этом модуле
    return user_money
