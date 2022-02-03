# пролезет ли кирпич A B C в отверстие D E
A, B, C = int(input()), int(input()), int(input())
D, E = int(input()), int(input())
if min(D, E) < min(A, B, C):
	print("NO")
else:
	print("YES")
