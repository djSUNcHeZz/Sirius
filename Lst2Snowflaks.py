'''
Снежинка
Дано нечётное число n.
Создайте двумерный массив из 𝑛×𝑛 элементов,
заполнив его символами "." (каждый элемент массива является строкой из одного символа).
Затем заполните символами "∗"
среднюю строку массива,
средний столбец массива,
главную диагональ
и побочную диагональ.
Для этого не нужно использовать вложенные циклы.
В результате символы "звёздочка" в массиве должны образовывать изображение снежинки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
'''
n = int(input())
D = []
for i in range(-n//2+1, n//2+1):
	D.append('.'*abs(n//2-abs(i))+'*'+'.'*(abs(i)-1)+'*'+'.'*(abs(i)-1)+'*'+'.'*abs(n//2-abs(i)))
D[n//2] = ['*' for elem in range(n)]

for row in D:
	print(*row)
