'''
Страницы книги
На каждой странице книги напечатано ровно k строк: на первой странице находятся строки с 1
Определите, на какой странице находится строка номер
n и какой по счёту будет эта строка на странице.
'''
k = int(input())
n = int(input())
print((k+n-1)//k, (n-1)%k+1)
