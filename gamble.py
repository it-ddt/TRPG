import os
import random
import show_player


def show_location(user_name, user_money, user_hp, user_luck, user_inventory, game):
    # TODO: удача игрока как-то должна влтиять на вероятность выигрыша, проигрыша
    # чем больше удача, тем больше минимальное число на костях, но не больше 12 

    # главный цикл модуля
    # заканчивается, если игрок выберет вернуться в лагерь
    is_busy = True
    while is_busy:
        os.system("cls")
        show_player.show(user_name, user_money, user_hp, user_luck, user_inventory, game)
        print(f"{user_name} зашел в логово разбойников и сел за игорный стол.")
        print("1 — Сделать ставку")
        print("2 — Вернуться в лагерь")

        # игрок выбирает вариант
        user_choice = input("Что делать? ")

        # делаем ставку и пытаемся на нее сыграть
        if user_choice == "1":
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

        # уходим в лагерь
        elif user_choice == "2":
            is_busy = False
            print(f"{user_name} отправился в лагерь.")

        # все остальные варианты
        else:
            print("Такого варианта нет, попробуйте другой.")

        input("ENTER — дальше")

    return user_money
