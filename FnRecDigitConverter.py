'''
Рекурсивный перевод
Напишите рекурсивную процедуру для перевода десятичного числа в 𝑃-ичную систему счисления.
В данной задаче запрещено использовать циклы и массивы.
Входные данные
На вход программе сначала подается значение 𝑃 (1<𝑃<10), а во второй строке — десятичное число.
Выходные данные
Вывод осуществляйте следующим образом:
сначала выведите введённое число в десятичной системе счисления,
за ним укажите его систему счисления в круглых скобках, то есть (10),
затем поставьте знак "=", после чего выведете результат работы вашей программы —
число в 𝑃-ичной системе счисления, за ним укажите его систему счисления в круглых скобках.
Весь вывод осуществляется без пробелов.
'''
def digit_convert(P, X):
	'''переводит число X в Р-ичную систему счисления'''
	global result
	if X > 1:
		digit_convert(P, X//P)
	result += str(X%P)
	return result
		
		
result, P, X = '', input(), input()
print(X+'(10)=' + digit_convert(int(P), int(X)).lstrip('0') + '('+P+')')
