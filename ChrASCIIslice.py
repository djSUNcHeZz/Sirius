'''
Символы в заданном интервале
Выведите подряд, без пробелов, все символы, лежащие в таблице ASCII между двумя заданными символами.
Входные данные
Программа получает на вход два символа, каждый в отдельной строке.
Выходные данные
Программа должна вывести строку, начинающуюся первым из заданных символов и заканчивающуюся вторым.
'''
for symbol in range(ord(input()), ord(input())+1):
	print(chr(symbol), end='')
