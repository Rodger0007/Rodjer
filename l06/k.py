import random 
player1 = {"счет":0,"ставка":0,"сумма":1000, "бросок":0} 
player2 = {"счет":0,"ставка":0,"сумма":1000, "бросок":0} 
player1["имя"] = input("Кем представишься?: ") 
player2["имя"] = input("Давй же, назови себя: ") 

while True: 
player1["ставка"] = int(input("Готов обанкротиться, ставь: ")) 
if player1["ставка"] > player1["сумма"]: 
player1["ставка"] = player1["сумма"] 
print("Ва-банк") 

player2["ставка"] = player1["ставка"]
if player2["ставка"] > player2["сумма"]: 
player2["ставка"] = player2["сумма"] 
print("Ва-банк - смело, но глупо!") 

player1["бросок"] = random.randint(0,10) 
player2["бросок"] = random.randint(0,10) 
print(player1["имя"],player1["бросок"]) 
print(player2["имя"],player2["бросок"]) 

if player1["бросок"] > player2["бросок"]: 
print(player1["имя"],"выиграл ставку!") 
player1["сумма"] += player2["ставка"] 
player2["сумма"] -= player2["ставка"] 

elif player2["бросок"] > player1["бросок"]: 
print(player2["имя"],"выиграл ставку!") 
player2["сумма"] += player1["ставка"] 
player1["сумма"] -= player1["ставка"] 
else: 
print("Ничья!") 
print(player1["имя"], player1["сумма"]) 
print(player2["имя"], player2["сумма"]) 
if player1["сумма"] <= 0: 
print(player2["имя"], "победил!") 
print(player1["имя"],"Ты лох") 
break 

if player2["сумма"] <= 0: 
print(player1["имя"], "победил!") 
print(player2["имя"],"Ты лох") 
break