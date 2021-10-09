import dice


def show_location_home():
	user_money = 5000  # деньги не должны переопределяться с каждым вызовом этой функции

	# пишем, что можно тут делать
	print("1 - ничего не делать")
	print("2 - сыграть в кости с разбойниками")
	
	# выбираем вариант
	user_choice = "0"
	while user_choice not in ("1", "2"):
		user_choice = input("Что делать? ")

	if user_choice == "1":
		print("Z-z-z")
	elif user_choice == "2":
		user_money = dice.play_dice(user_money)
		print("У тебя теперь", user_money)
	else:
		print("Что-то пошло не так")


show_location_home()
