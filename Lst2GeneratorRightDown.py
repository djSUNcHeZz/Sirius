'''
Слева направо, сверху вниз
Даны два числа 𝑛 и 𝑚
Создайте двумерный массив размером 𝑛×𝑚
и заполните его в соответствии с примером.
'''
n, m = list(map(int, input().split()))
A = [[x+y*m for x in range(m)] for y in range(n)]
for i in range(n):
    for j in range(m):
        print(A[i][j], end = ' ')
    print()
