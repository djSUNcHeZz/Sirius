'''
Лесенки
Каждый следующий горизонтальный слой содержит меньше кубиков, чем слой под ним.
Требуется подсчитать количество различных лесенок, которые могут быть построены ровно из 𝑁 кубиков.
'''
def count_lesenka(N, k):
	'''выводит количество различных лесенок из N кубиков'''
	res = 0
	if N == 0:
		return res+1
	elif N > k:
		for i in range(k+1, N+1):
			res += count_lesenka(N-i, i)
		return res
	else:
		return res
	
print(count_lesenka(int(input()), 0))
