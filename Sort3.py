# упорядочить 3 числа
a, b, c = int(input()), int(input()), int(input())
if c < a:
	a, c = c, a
if b < a:
	a, b = b, a
if b > c:
	c, b = b, c
print(a, b, c)
