'''
Несправедливые башни
В Ханое несправедливо запретили класть самый маленький диск (номер 1) на средний колышек (номер 2).
'''
def hanoy_1(a, b, c):
	if a == 1:
		print(a, b, c)
	else:
		hanoy_1(a-1, b, c)
		print(a, b, 6-b-c)
		hanoy_1(a-1, c, b)
		print(a, 6-b-c, c)
		hanoy_1(a-1, b, c)

		
hanoy_1(int(input()),1 , 3)
