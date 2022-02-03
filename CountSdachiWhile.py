'''
Выдача сдачи циклом while
Имеется неограниченное количество монет в 1, 2, 5, 10 рублей.
Определите, сколькими способами можно выдать сдачу в 𝑛 рублей.
Например, 5 рублей можно выдать четырьмя способами: 5=2+2+1=2+1+1+1=1+1+1+1+1
Входные данные
Программа получает на вход натуральное число 𝑛 , не превышающее 10**6
'''
n = int(input())
counter = five = 0
while five <= n:
	ostatok = n - five
	counter += (ostatok//2+1)*(five//10+1)
	five += 5
print(counter)
	
'''
# bool bruteforce
n = int(input())
counter = one = two = five = ten = 1
while ten*10 <= n:
	five = int(five == 22) or five
	two = int(two == 52) or two
	one = int(one == 102) or one
	#print(ten-1, five-1, two-1, one-1)
	counter += ((ten-1)*10+(five-1)*5+(two-1)*2+(one-1)*1 == n)
	one += (one < 103)
	two += (one == 102)
	five += (two == 52)
	ten += (five == 22)
print(counter-1)
'''
