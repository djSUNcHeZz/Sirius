'''
Сортирующие башни
Первоначально все диски лежат на стержне номер 1.
Переместите диски с нечётными номерами на стержень номер 2,
а с чётными номерами — на стержень номер 3
'''


def hanoy(n, x, y):
	tmp = 6 - x - y
	if n > 0:
		hanoy(n - 1, x, tmp)
		print(n, x, y)
		hanoy(n - 1, tmp, y)


def hanoy_sort(n, x, y):
	tmp = 6 - x - y
	if n > 0:
		hanoy(n - 1, x, tmp)
		print(n, x, y)
		if n > 3:
			hanoy(n - 3, tmp, x)
		if n > 2:
			print(n - 2, tmp, y)
		if n > 3:
			hanoy_sort(n - 3, x, tmp)


n = int(input())
hanoy_sort(n, 1, 3) if n % 2 == 0 else hanoy_sort(n, 1, 2)

