'''
Количество разбиений на слагаемые
Дано натуральное число 𝑁
Найдите количество его разбиений на натуральные слагаемые.
Два разбиения, отличающиеся только порядком слагаемых, будем считать за одно.
Например, для 𝑁=5 существует 7 различных разбиений:
5=5
5=4+1
5=3+2
5=3+1+1
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Входные данные
Задано единственное число 𝑁≤30
Выходные данные
Выведите количество различных разбиений на слагаемые.
'''
def count_slag(n, k):
	'''выводит k-количество разбиений на слагаемые числа n'''
	if n == 0:
		return 1
	res = 0
	for i in range(1, min(n, k)+1):
		res += count_slag(n-i, i)
	return res


n = int(input())	
print(count_slag(n, n))
