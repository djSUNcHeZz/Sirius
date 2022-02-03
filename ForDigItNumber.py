# разбиение числа с конца на цифры
n = int(input())
for i in range(len(str(n))):
	print(n//10**i %10, end='')

print()
for i in range(len(str(n))):
	print(n%10, end='')
	n //= 10 # отбрасываем последнюю цифру
