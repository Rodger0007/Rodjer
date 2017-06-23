geometria = {"Теорема Пифагора": "kek","Равенства треугольников":"ууууу"}
print(geometria["Теорема Пифагора"])

s = 0
while s < 10:
	s += 1 
	if s == 5:
		continue 
	print(s)

good_boys = ["Ибрагим", "Халид", "Сааду"]
for boy in good_boys:
	print(boy)

for number in "10":
	print(number)

user = {
	"Имя":"Вова",
	"кошка": True,
	"деньги": 100
}

for el in user:
	print(el, user[el])

# for value in user.value():
# 	print(value)

for key, value in user.items():
	print(key, value)

for i in range(5,10,2):
	print(i)