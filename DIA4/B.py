t = int(input())

num = [1, 7, 17, 119, 289, 2023]

for _ in range(t):
	n, k = tuple(map(int, input().split()))
	b = tuple(map(int, input().split()))

	res = 1
	for bi in b:
		res*=bi

	lis = []
	if res in num:
		while res < 2023:
			if res*17 <= 2023:
				res *= 17
				lis.append(17)
				k -= 1
			elif res*7 <= 2023:
				res *= 7
				lis.append(7)
				k -= 1
			else:
				lis.append(1)
				k -= 1

		print("yes\n" + " ".join(map(str, lis)))
	else:
		print('no')

"""
7
2 2
5 2
3 1
7 17 7
4 1
1 17 1 1
3 1
7 17 17
1 1
289
1 1
2023
1 3
1

1
7 			7 * 17 * 17 = 2023
17  		17 * 119 = 2023
119			119 = 17 * 7
289 		289 = 17 * 17 || 289 * 7 = 2023
2023
"""