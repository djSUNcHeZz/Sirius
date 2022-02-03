'''
Треугольник
Вам даны 4 отрезка.
Выведите YES, если среди них найдутся 3, из которых можно составить треугольник,
и NO в противном случае.
Для решения напишите функцию triangle(a, b, c), которая будет возвращать True, если из трёх заданных отрезков можно составить треугольник, и False иначе.
'''
def triangle(a, b, c):
	return (a+b-c > 0 and b+c-a > 0 and c+a-b > 0)


a, b, c, d = int(input()), int(input()), int(input()), int(input())
print ('YES' if triangle(a,b,c) or triangle(a,b,d) or triangle(a,c,d) or triangle(b,c,d) else 'NO')
