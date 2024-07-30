from collections import deque

t = int(input())

nums = []
for i in range(t):
	A, B = input().split()
	ships = int(A)
	damage = int(B)
	res = deque(map(int, input().split()))
	amount = 0

	while len(res) > 0 and res[0] + res[-1] <= damage:
		if len(res) > 1 and res[0] == res[-1]:
			min = res[0]
			res.popleft()
			res.pop()
			damage -= min
			damage -= min
			amount += 2
		elif res[0] < res[-1]:
			popp = res.popleft()
			damage -= popp * 2
			if len(res) != 0:
				res[-1] -= popp
			amount += 1
		else:
			popp = res.pop()
			damage -= popp * 2
			if len(res) != 0:
				res[0] -= popp
			amount += 1

	if len(res) > 0 and damage - res[0] > res[-1]:
		amount += 1

	if len(res) > 0 and (res[0] <= damage or ((res[0] + res[-1]) == damage)):
		amount += 1

	print(amount)
"""
6
4 5
1 2 4 3
4 6
1 2 4 3
5 20
2 7 1 8 2
2 2
3 2
2 15
1 5
2 7
5 2

"""