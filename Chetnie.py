'''
вывести четные числа
'''
a, b = int(input()), int(input())
s = (a%2!=0)
for i in range(a+s, b+1, 2):
	print(i, end=' ')
