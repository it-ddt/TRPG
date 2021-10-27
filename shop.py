def show_location_shop(money, inventory):
    potion_prise = 50
    print(f"1 - купить зелье здоровья за {potion_prise}")
    print("2 - посмотреть инвентарь")
    print("3 - пойти домой")

    user_choise = "0"
    while user_choise not in ("1", "2", "3"):
        user_choise = input("Что делать? ")

    if user_choise == "1" and money >= potion_prise:
        money -= potion_prise
        inventory.append("зелье здоровья")
        print("купил зелье здоровья")
        show_location_shop(money, inventory)
    elif user_choise == "1" and money < potion_prise:
        print("маловато денег")
        show_location_shop(money, inventory)
    elif user_choise == "2":
        for i in inventory:
            print(i)
        show_location_shop(money, inventory)
    else:
        print("вышел")