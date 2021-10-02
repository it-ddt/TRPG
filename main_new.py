import os
import random

user_name = "Вася"
user_money = 5000


def show_location_home():
    # описываем место
    os.system("cls")
    print("Вы дома")
    print("1 - в казино")
    print("2 - ждать")

    # спросить пользователя
    user_choice = ""
    while user_choice not in ("1", "2"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    # проверить ответ пользователя
    if user_choice == "1":
        show_location_casino()
    else:
        print("жду")
        os.system("cls")
        show_location_home()


def show_location_casino():
    # описываем место
    os.system("cls")
    print("Вы в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - сыграть")

    # спросить пользователя
    user_choice = ""
    while user_choice not in ("1", "2", "3"):
        user_choice = input("введите номер варианта и нажмите Enter ")

    # проверить ответ пользователя
    if user_choice == "1":
        show_location_home()
    elif user_choice == "2":
        print("жду")
        os.system("cls")
        show_location_casino()
    else:
        show_gamble()


def show_gamble():
    global user_money
    casino_bet = 50
    print("Сейчас у вас", user_money, "денег")
    user_dice = random.randint(2, 12)
    casino_dice = random.randint(2, 12)
    print(f"Вы бросили кости, выпало {user_dice}")
    print(f"Казино кости, выпало {casino_dice}")
    if user_dice > casino_dice:
        print("Вы победили")
        user_money += casino_bet
    elif user_dice < casino_dice:
        print("Вы проиграли")
        user_money -= casino_bet
    else:
        print("Ничья")
    print("Теперь у вас", user_money, "денег")
    input("Нажмите ENTER чтобы вернуться в казино")
    show_location_casino()


# игра началась здесь
show_location_home()
