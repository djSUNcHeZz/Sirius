'''
вывести количество нулей
'''
count = 0
for i in range(int(input())):
	x = int(input())
	count += (x==0)
print(count)
