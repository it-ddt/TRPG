def save(user_name, user_money, user_hp, user_luck, user_inventory):
    with open("save", "w", encoding="utf-8") as file:
        file.write(user_name + "\n")
        file.write(str(user_money) + "\n")
        file.write(str(user_hp) + "\n")
        file.write(str(user_luck) + "\n")
        for item in user_inventory:
            file.write(item + "\n")

def load():
    hero_list = []
    return hero_list