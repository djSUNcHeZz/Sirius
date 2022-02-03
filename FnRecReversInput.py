def reverse_input():
	'''разворот вводимой последовательности,
	оканчивающейся нулем'''
	n = int(input())
	if n != 0:
		reverse_input()
	print(n)
	
reverse_input()
