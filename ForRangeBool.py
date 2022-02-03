# вывод прямой или обратной последовательности от А до В
A, B = int(input()), int(input())
s = (A < B) or -1
for i in range(A, B+s, s):
	print(i, end=' ')
