'''
Шахматная доска
Шахматная доска состоит из n×m клеток, покрашенных в чёрный и белый цвет в шахматном порядке.
При этом клетка в левом нижнем углу доски покрашена в чёрный цвет.
Определите, сколько всего на доске чёрных клеток
'''
n = int(input())
m = int(input())
print((n*m+1)//2)