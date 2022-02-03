# Простое или составное число
def min_divisor(n):
	'''возвращает минимальный делитель'''
	divisor = 2
	while n % divisor != 0:
		divisor += 1
	return divisor


def is_prime(n):
	'''возвращает True если простое число
	и False - если составное'''
	return min_divisor(n) == n


n = int(input())
print('Минимальный делитель -', min_divisor(n))
print('Простое' if is_prime(n) else 'Составное')

