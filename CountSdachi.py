'''
Выдача сдачи
Имеется неограниченное количество монет в 1, 2 , 5, 10 рублей.
Определите, сколькими способами можно выдать сдачу в 𝑛 рублей.
Например, 5 рублей можно выдать четырьмя способами: 5=2+2+1=2+1+1+1=1+1+1+1+1
Входные данные
Программа получает на вход натуральное число 𝑛 , не превышающее 100
'''
n = int(input())
counter = 0
for ten in range(10):
	for five in range(20):
		for two in range(50):
			for one in range(100):
				counter += (ten*10+five*5+two*2+one*1 == n)
print(counter)
