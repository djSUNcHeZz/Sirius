'''
Делёж яблок — 2
n школьников делят k яблок “почти поровну”, то есть так,
чтобы количество яблок, доставшихся любым двум школьникам,
отличалось бы не более, чем на 1
Программа должна вывести количество школьников,
которым достанется яблок меньше, чем некоторым из их товарищей.
'''
n = int(input())
k = int(input())
print((n-k%n)%n)
