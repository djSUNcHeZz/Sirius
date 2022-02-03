'''
Линейное уравнение
Даны числа a и b. Решите в целых числах уравнение ax+b=0
Выведите все целочисленные решения этого уравнения, если их число конечно,
выведите слово NO, если решений нет,
выведите слово INF, если целочисленных решений бесконечно много.
'''
a, b = int(input()), int(input())
if a == 0:
	if b == 0:
		print('INF')
	else:
		print('NO')
elif b%a == 0:
	print(-b//a)
else:
	print('NO')