'''
Количество элементов, которые больше предыдущего
Последовательность состоит из натуральных чисел и завершается числом 0
Определите, сколько элементов этой последовательности больше предыдущего элемента.
'''
n1, n2 = int(input()), int(input())
count = 0
while n2 !=0:
	count += (n2 > n1)
	n1 = n2
	n2 = int(input())
print(count)
