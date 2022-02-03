'''
Палиндром
Вывод YES если строка палиндром
'''
S = input()
print('YES' if S[:] == S[::-1] else 'NO')
