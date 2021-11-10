import os
import random

def show_location(user_name, user_money, user_luck):
    # TODO: удача игрока как-то должна влтиять на вероятность выигрыша, проигрыша
    # чем больше удача, тем больше минимальное число на костях, но не больше 12 
    is_gambling = True

    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    while is_gambling:
        
        9
        user_choise = "0"
        while user_choise not in ("1", "2"):
            os.system("cls")
            print(f"имя: {user_name}")
            print(f"деньги: {user_money}")
            print(f"удача: {user_luck}")
            print("----------")
            print(f"{user_name} зашел в логово разбойников и сел за игорный стол.")
            print("1 — Сделать ставку")
            print("2 — Вернуться в лагерь")
            user_choise = input("Что делать? ")

        # проверяем выбор игрока

        # делаем ставку и пытаемся на нее сыграть
        if user_choise == "1":
            # TODO: сделать проверку ставки, она должна быть целым числом
            user_bet = int(input("Сколько поставить на кон? "))
            
            # слишком большая ставка, не играем
            if user_bet > user_money:
                print(f"У {user_name} нет столько денег!")
            
            # слишком маленькая ставка, не играем
            elif user_bet < 1:
                print(f"Ставка должна быть больше нуля!")
            
            # подходящая ставка, играем!
            else:
                user_score = random.randint(2, 12)
                casino_score = random.randint(2, 12)
                print(f"{user_name} выбросил {user_score}")
                print(f"Разбойник выбросил {casino_score}")

                # проверяем результат игры

                # пользователь выиграл
                if user_score > casino_score:
                    user_money += user_bet
                    print(f"Ура! {user_name} выиграл {user_bet}!")

                # пользователь проиграл
                elif user_score < casino_score:
                    user_money -= user_bet
                    print(f"Эх! {user_name} проиграл {user_bet}!")

                # ничья
                else:
                    print("Ничья!")

            input("ENTER — дальше")

        # уходим в лагерь
        else:
            is_gambling = False
            print(f"{user_name} отправился в лагерь.")

    return user_money
