'''
Вставка символов
Дана строка. Получите новую строку,
вставив между всеми парами соседних символов исходной строки символ ∗
'''
S = input()
for i in range(len(S)-1):
	print(S[i], '*', sep='', end='')
print(S[-1])
