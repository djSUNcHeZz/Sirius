'''
Больше своих соседей
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
'''
S = list(map(int, input().split()))
counter = 0
for i in range(1,len(S)-1):
	counter += (S[i] > S[i-1] and S[i] > S[i+1])
print(counter)
