# выведите четные элементы списка
S = list(map(int, input().split()))
print(*[x for x in S if x%2 ==0])
'''
# олдскул
for x in S:
	print(str(x)+" " if x%2 == 0 else "", end="")
'''
# вывод элементов с четным индексом
S = list(map(int, input().split()))
print(*[S[i] for i in range(0,len(S),2)])
