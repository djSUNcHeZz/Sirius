def power_fast(x, n):
	if n == 0:
		return 1
	elif n%2 == 1:
		return power_fast(x, n-1) * x
	else:
		return power_fast(x*x, n//2)
		

print(power_fast(float(input()), int(input())))


def pow(a:float, n:int):
	'''возведение в степень с ускорением по квадрату числа'''
	if n == 0:
		return 1
	elif n%2 == 1: #нечетная степень
		return pow(a, n-1)*a
	else: #четная степень
		return pow(a**2, n//2)
		
		
print(pow(float(input('Введи любое число:')), int(input('Введи целую степень:'))))
