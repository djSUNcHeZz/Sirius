'''
Кинотеатр
В кинотеатре 𝑛 рядов по 𝑚 мест в каждом. В двумерном массиве хранится информация о проданных билетах, число 1 означает, что билет на данное место уже продан, число 0 означает, что место свободно.
Поступил запрос на продажу 𝑘 билетов на соседние места в одном ряду.
Определите, можно ли выполнить такой запрос.
Входные данные
Программа получает на вход числа 𝑛≤30 и 𝑚≤30
Далее идут 𝑛 строк, содержащих 𝑚 чисел (0 или 1), разделённых пробелами.
Затем дано число 𝑘
Выходные данные
Программа должна вывести номер ряда, в котором есть 𝑘 подряд идущих свободных мест.
Если таких рядов несколько, то выведите номер наименьшего подходящего ряда.
Если подходящего ряда нет, выведите число 0
'''
n, m = map(int, input().split()) #загружаем строку из двух чисел: ряд и место
D = [list(map(int, input().split())) for i in range(n)] #загружаем строки таблицы
k = int(input()) #кол-во билетов
res = 0
for y in range(n):
	counter = 0
	for x in range(m):
		if D[y][x] == 0:
			counter += 1 #считаем пустые места подряд
			if counter == k:
				res = y+1
		else:
			counter = 0 #сбрасываем счетчик если места не подряд
	if res > 0: #выходим для вывода наименьшего ряда
		break
print(res)
