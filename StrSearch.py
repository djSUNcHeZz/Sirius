'''
Совпадающие начало и конец
Дана строка. Требуется найти самую длинную её подстроку, у которой совпадает первый и последний символы. 
Если подходит несколько подстрок, то выведите любую из них.
'''
S = input()
result = ''
for i in range(len(S)):
	j = S.rfind(S[i])+1
	if len(result) < j-i:
		result = S[i:j]
print(result)
