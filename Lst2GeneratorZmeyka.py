'''
Заполнение змейкой
По данным числам 𝑛 и 𝑚 заполните двумерный массив размером 𝑛×𝑚 числами от 1 до 𝑛×𝑚 “змейкой”
'''
n, m = map(int, input().split())
D = [[1+x+y*m for x in range(m)][::-1+(y%2 == 0)*2] for y in range(n)] #логический разворт нечетных строк
for s in D:
	print(*s)
