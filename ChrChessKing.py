'''
Ход короля и шахматная нотация
Шахматный король ходит по горизонтали, вертикали и диагонали, но только на одну клетку.
Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.
Входные данные
Входной файл состоит из двух строк — координат первой и второй клетки в шахматной нотации.
Как известно, в шахматной нотации горизонтальные строки обозначаются цифрами от 1 до 8,
считая от расположения белых фигур, стоящих внизу доски,
а вертикальные столбцы — буквами латинского алфавита: 𝑎,𝑏,𝑐,𝑑,𝑒,𝑓,𝑔,ℎ
Выходные данные
Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую,
или NO в противном случае.
'''
pos1, pos2 = input(), input()
print('YES' if abs(ord(pos1[0]) - ord(pos2[0])) < 2 and abs(ord(pos1[1]) - ord(pos2[1])) < 2 else 'NO')
