import os
import random


def play_dice(money: int) -> int:
    """
        Принимает деньги пользователя.
        Возвращает измененные деньгим пользователя 
        после выигрышей или проигрышей.

        TODO:
            Передать сюда параметр удачи.
            Он должен влиять на минимальное значение костей пользователя.
            Написать исключения при попытке интовать ставку.
    """
    
    # Очищаем экран, печатаем деньги пользователя
    # и описываем возможные варианты.
    os.system("cls")
    print(f"У тебя {money}")
    print("1 - сделать ставку")
    print("2 - уйти домой")


    # Выбираем вариант, пока он не будет одним из возможных.
    user_choise = "0"
    while user_choise not in ("1", "2"):
        user_choise = input("Что делать? ")

    # Делаем ставку и проверяем ее.
    # При неправильной ставке предлагаем ставить заново.
    if user_choise == "1":
        bet = int(input("Сколько ставишь? "))  # FIXME: не все интуется, например Вася

        if bet > money:  # Ставим не больше, чем есть у игрока.
            print("У тебя столько нет!")
            input("Нажми ENTER для продолжения")
            play_dice(money)
        elif bet <= 0:  # Нельзя поставить 0 и меньше.
            print("Ставки от 1!")
            input("Нажми ENTER для продолжения")
            play_dice(money)
        else:
            user_dice = random.randint(2, 12)
            computer_dice = random.randint(2, 12)

            # Печатаем результаты и проверяем выпавшее.
            print(f"Ты выбросил {user_dice}")
            print(f"Разбойник выбросил {computer_dice}")
            if user_dice > computer_dice:
                print("Ты выиграл")
                money += bet
            elif user_dice == computer_dice:
                print("Ничья")
            else:
                print("Ты проиграл!")
                money -= bet
            print("У тебя", user_money)
            input("Нажми ENTER для продолжения")
            play_dice(money)
    else:
        print("Ты пошел домой")
        input("Нажми ENTER для продолжения")

    return money
