import random


def play_dice(user_money):
	bet = int(input("Сколько ставишь? "))  # FIXME: не все интуется, например Вася

	# тест ставки
	if bet > user_money:
		print("У тебя столько нет!")
		play_dice(user_money)
	elif bet <= 0:
		print("Ставки от 1!")
		play_dice(user_money)
	else:
		user_dice = random.randint(2, 12)
		casino_dice = random.randint(2, 12)
		
		# проверить выпавшее
		print("У вас", user_dice)
		print("У разбойника", casino_dice)
		if user_dice > casino_dice:
			print("Ты выиграл")
			user_money += bet
		elif user_dice == casino_dice:
			print("Ничья")
		else:
			print("Ты проиграл!")
		return user_money
