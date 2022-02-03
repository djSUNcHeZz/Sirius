'''
Ход коня
'''
y1, x1, y2, x2 = int(input()), int(input()), int(input()), int(input())
dy, dx = abs(y1-y2), abs(x1-x2)
print('YES' if (dy == 1 and dx == 2) or (dy == 2 and dx == 1) else 'NO')
