'''
Номер числа Фибоначчи
Дано натуральное число 𝐴
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число 𝑛
Если 𝐴 не является числом Фибоначчи, выведите число −1
'''
number = int(input())
count, first, second = 0, 0, 1
while first <= number:
	result = count*(first == number) or -1
	count += 1
	first, second = second, first + second
result = int(count == 1) or result
print(result)
