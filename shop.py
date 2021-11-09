import os


def show_location_shop(name: str, money: int, inventory: list) -> list:
    
    potion_prise = 50
    os.system('cls')
    print(f"{name} в лавке торговца зельями. У него {money} монет.")
    print("В инвентаре:")
    for i in inventory:
            print(i)
    print("")
    print(f"1 - купить зелье здоровья за {potion_prise}")
    print("2 - пойти домой")

    user_choise = "0"
    while user_choise not in ("1", "2"):
        user_choise = input("Что делать? ")

    if user_choise == "1" and money >= potion_prise:
        money -= potion_prise
        inventory.append("зелье здоровья")
        print("купил зелье здоровья")
        show_location_shop(name, money, inventory)
    elif user_choise == "1" and money < potion_prise:
        print("Маловато денег!")
        show_location_shop(name, money, inventory)
    elif user_choise == "2":
        hero = "dfasdfasdasdfsa"
        return hero
    else:
        return "Error"

# FIXME: почему-то возвращает None