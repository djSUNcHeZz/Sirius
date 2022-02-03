'''
Шашку — в дамки
На шахматной доске (8×8) стоит одна белая шашка.
Сколькими способами она может пройти в дамки?
(Белая шашка ходит по диагонали. на одну клетку вверх-вправо или вверх-влево.
Шашка проходит в дамки, если попадает на верхнюю горизонталь.)
Входные данные
Вводятся два числа от 1 до 8:
номер номер столбца (считая слева) и строки (считая снизу),
где изначально стоит шашка.
Выходные данные
Вывести одно число — количество путей в дамки.
'''

#через рекурсию
def get_var(x, y, N):
	'''выводит количество вариантов
	прохода в дамки с позиции x y'''
	if y == 8:
		return N
	if x == 1:
		return get_var(2, y + 1, N)
	if x == 8:
		return get_var(7, y + 1, N)
	return (get_var(x + 1, y + 1, N) + get_var(x - 1, y + 1, N))


x, y = map(int, input().split())
print(get_var(x, y, 1))
