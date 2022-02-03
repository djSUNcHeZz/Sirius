'''
Поменять местами две диагонали
Дан квадратный массив.
Поменяйте местами в каждом столбце элементы, стоящие на главной и побочной диагонали.
Входные данные
В первой строке дано число 𝑛≤10
Далее идут 𝑛 строк по 𝑛 неотрицательных целых чисел не больше 100
'''
n = int(input())
D = [list(map(int, input().split())) for i in range(n)] #загружаем строки таблицы
for i in range(n):
	D[i][i], D[n-1-i][i] = D[n-1-i][i], D[i][i]
for i in D:
	print(*i)
