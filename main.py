import os  # для очистки экрана
import dice  # для игры в кости
import shop  # для покупки зелий


def show_location_home(user_name: str, user_money: int, user_inventory: list):
    """
        Принимает деньги пользователя.
        Очищает экран и печатает варианты действий.
        Дает выбирать из этих действий.
        Игра завершается, если переменная game тановится False.
        
        TODO:
            Передать сюда все параметры пользователя.
            Печатать параметры пользователя.
            Пробросить user_luck в игру в кости.
            Использовать user_name место Ты/Вы.
            Использовать переменную game для выхода из игры.

            Подключить модули Арены и Магазина.
    """

    # Очищаем экран и описываем возможные варианты.
    os.system("cls")
    print(f"имя: {user_name}")
    print(f"деньги: {user_money}")
    print(f"удача: {user_luck}")
    print(f"здоровье: {user_hp}")
    print("инвентарь:")
    for i in user_inventory:
            print(i)
    print()
    print(f"{user_name} дома. Что ему делать?")
    print("1 - ничего не делать")
    print("2 - сыграть в кости с разбойниками")
    print("3 - пойти в магазин зелий")
    print("4 - выйти из игры")

    # Выбираем вариант, пока он не будет одним из возможных.
    user_choice = "0"
    while user_choice not in ("1", "2", "3", "4"):
        user_choice = input("Что делать? ")

    # Действуем по выбранному пользователем варианту.
    if user_choice == "1":
        print(f"{user_name} пялился в стену и вкоре задремал")
        input("Нажми ENTER для продолжения")
        show_location_home(user_name, user_money, user_inventory)
    elif user_choice == "2":
        user_money = dice.play_dice(user_name, user_money)
        show_location_home(user_name, user_money, user_inventory)
    elif user_choice == "3":
        print(f"{user_money} до вызова лавки")
        user_hero = shop.show_location_shop(user_name, user_money, user_inventory)
        user_money = user_hero[0]
        user_inventory = user_hero[1]
        show_location_home(user_name, user_money, user_inventory)
    elif user_choice == "4":
        print("Выходим из игры")
    else:
        print("Что-то пошло не так")

    # Чтобы экран не очистился раньше, чем пользователь увидит
    # результат своих действий.
    input("Нажми ENTER для продолжения")


# создаем персонажа
user_name = "Вася Питонов"
user_money = 5000
user_luck = 30
user_hp = 100
user_inventory = ["меч", "щит"]
game = True

# начинаем играть
show_location_home(user_name, user_money, user_inventory)
