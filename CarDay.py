'''
За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?

Используем округление в большую сторону
'''
n = int(input())
m = int(input())
print((m+n-1)//n)
