'''
Сменить регистр символа
Напишите функцию CaseChange (c), меняющую регистр символа,
то есть переводящую заглавные буквы в строчные, а строчные — в заглавные,
остальные символы меняться не должны.
В решении нельзя использовать циклы.
В решении нельзя использовать константы с неочевидным значением.
'''


def CaseChange(c):
	'''преобразует символы в противоположный регистр'''
	return c.lower() if c.isupper() else c.upper()


a = input()
ans = CaseChange(a)
print(ans)
