'''
Остатки
Даны целые неотрицательные числа a, b, c, d, при этом 0≤𝑐<𝑑
Выведите в порядке возрастания все числа от 𝑎 до 𝑏, которые дают остаток 𝑐 при делении на 𝑑
В этой задаче нельзя использовать инструкцию if, операторы сравнения (< и т.д.), должен быть только один цикл
'''
a, b, c, d = int(input()), int(input()), int(input()), int(input())
a = (a-c + d-1)//d*d + c
for i in range(a, b+1, d):
	print(i, end=' ')
