'''
Яша плавает в бассейне
Яша плавал в бассейне размером 𝑁×𝑀
метров и устал. В этот момент он обнаружил, что находится на расстоянии 𝑥
метров от одного из длинных бортиков (не обязательно от ближайшего) и 𝑦
метров от одного из коротких бортиков.
Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
'''
N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N > M:
	N, M = M, N
s = x
if N-x < s:
	s = N-x
if y < s:
	s = y
if M-y < s:
	s = M-y
print(s)