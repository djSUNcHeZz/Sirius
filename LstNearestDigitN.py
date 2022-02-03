'''
Ближайшее число
Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.
Входные данные
В первой строке содержатся список чисел — элементы массива (целые числа, не превосходящие 1000 по абсолютному значению).
Во второй строке вводится одно целое число 𝑥, не превосходящее 1000 по абсолютному значению.
Выходные данные
Вывести значение элемента массива, ближайшего к 𝑥
Если таких чисел несколько, выведите любое из них.
'''
S = list(map(int, input().split()))
x = int(input())
result = S[0]
for i in S:
	if abs(i - x) < abs(result - x):
		result = i
print(result)