'''
Количество совпадающих пар
Дан список чисел. Посчитайте, сколько в нём пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
'''
S = [i for i in input().split()]
counter = 0
for n in range(len(S)-1):
	counter += S[n+1:].count(S[n])
#	for m in range(n+1, len(S)):
#		counter += (S[n] == S[m])
print(counter)