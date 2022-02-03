def faktorial(n):
	'''выводит факториал n'''
	return 1 if n == 0 else faktorial(n-1) * n
	
	
print(faktorial(int(input())))
