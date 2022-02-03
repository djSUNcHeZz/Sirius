'''
Минимальный простой делитель
'''

# прошла проверку на Сириусе
N = int(input())
s = 1 / 2
a = N
b = int(N**s)
for i in range(2, b + 1):
	if N % i == 0:
		if a > i:
			a = i
print(a)

# ищем через ряд фибоначи
'''
n = int(input())
first, second = 2, 3
delitel = first
while n % delitel != 0:
	print(delitel)
	if delitel*delitel <= n:
		delitel = first
		first, second = second, first + second
	else:
		delitel = n
		break
print()
print(delitel)
'''
