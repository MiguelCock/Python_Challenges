page_max = int(input().split()[1])
names_list = list(map(int, input().split()))

pages = []
amount = 0
for names in names_list:
	amount += names
	if amount > page_max:
		times = amount//page_max
		pages.append(times)
		amount = amount - (times*page_max)
	else:
		pages.append(0)

res = ' '.join(map(str, pages))
print(res)