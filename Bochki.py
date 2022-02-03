# подбор окончания в слове
# bochek 5-20 25-30
# bochki 2-4 22-24
# bochka 1 21
n = int(input())
if 5 <= n%100 <= 19 or 5 <= n%10 <= 9 or n%10 == 0:
	print(n, 'bochek')
elif 2 <= n%10 <= 4:
	print(n, 'bochki')
else:
	print(n, 'bochka')
