'''
Развернуть элементы с нечетными индексами
Вам дан список целых чисел.
Разверните элементы с нечетными индексами.
'''
S = [i for i in input().split()]
S[1::2] = S[1::2][::-1]
print(*S)
