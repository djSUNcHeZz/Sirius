'''
Переставить min и max
Дан список чисел. В списке все элементы различны.
Поменяйте местами минимальный и максимальный элемент этого списка.
'''
S = [int(i) for i in input().split()]
ind_min = S.index(min(S))
ind_max = S.index(max(S))
S[ind_min], S[ind_max] = S[ind_max], S[ind_min]
print(*S)
