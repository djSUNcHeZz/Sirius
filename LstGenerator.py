'''
Список степеней
Используя генератор, составьте список 𝑆
, заполненный степенями числа 𝑋 от 0 до 𝑁−1
и распечатайте его инструкцией print(S).
'''
'''
X, N = int(input()), int(input())
S = [X**i for i in range(N)]
print(S)
'''

'''
Вывести список в обратном порядке
'''
S = [int(i) for i in input().split()]
print(*S[::-1])
