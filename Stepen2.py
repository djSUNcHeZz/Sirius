'''
Точная степень двойки
Дано натуральное число 𝑁
Выведите слово YES, если число 𝑁 является точной степенью двойки,
или слово NO в противном случае.
Операцией возведения в степень пользоваться нельзя!
'''
n = int(input())
x = 1
while x*2 <= n:
	x *= 2
if x == n:
	print('YES')
else:
	print('NO')
