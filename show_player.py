def show(user_name, user_money, user_hp, user_luck, user_inventory, game):
    print(f"имя: {user_name}")
    print(f"деньги: {user_money}")
    print(f"жизни: {user_hp}")
    print(f"удача: {user_luck}")
    print(f"инвентарь:")
    for item in user_inventory:
        print(" •", item)
    print("")
