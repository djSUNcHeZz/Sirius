'''
Количество различных элементов — 2
Дан список. Посчитайте, сколько в нём различных элементов, не изменяя самого списка.
'''
S = [int(i) for i in input().split()]

print(len(set(S)))
