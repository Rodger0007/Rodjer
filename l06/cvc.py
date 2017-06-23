import random
player1 = {"Счет":0,"Ставка":0,"Сумма":1000,"Бросок":0}
player2 = {"Счет":0,"Ставка":0,"Сумма":1000,"Бросок":0}
player1["Имя"] = input("Введите имя 1-го игрока: ")
player2["Имя"] = input("Введите имя 2-го игрока: ")

player1["Ставка"] = input("Введите ставку")
if player1["Ставка"] > player1["Сумма"]:
	player1["Ставка"] = player1["Сумма"]

player2["Ставка"] = input("Введите ставку")
if player1["Ставка"] > player1["Сумма"]:
	player1["Ставка"] = player1["Сумма"]

player1["Бросок"] = random.randint(2:12)
player2["Бросок"] = random.randint(2:12)
print(player1["Имя"], player1"Бросок")
print(player2["Имя"], player2"Бросок")

if player1["Бросок"] > player2["Бросок"]:
	print(player1["Имя"],"Выиграл ставку!")
	player1["Сумма"] += player2["Сумма"]
	player2["Сумма"] -= player1["Сумма"]

elif player2["Бросок"] > player1["Бросок"]:
	print(player2["Имя"],"Выиграл ставку!")
	player2["Сумма"] += player1["Сумма"]
	player1["Сумма"] -= player2["Сумма"]
else:
	print("Ничья")
print(player1["Имя"], player1["Сумма"])
print(player2["Имя"], player2["Сумма"])
if player1["Сумма"] <= 0:
	print(player2["Имя"],"Выиграл ставку")