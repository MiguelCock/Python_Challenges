t = int(input())

for _ in range(t):
	A, B = input().split()
	A = int(A)
	B = int(B)

	total1 = min(A // 2, B // 2)
	total2 = min(A // 1, B // 3)
	total3 = min(A // 3, B // 1)

	m = min(A, B)
	A1 = A-(2*(m//2))
	B1 = B-(2*(m//2))

	if A1 == 1 and B1 >= 3:
		total1 += 1
	elif B1 == 1 and A1 >= 3:
		total1 += 1

	print(max(total1, total2, total3))
"""
6
5 5
10 1
2 3
0 0
17 2
1000000000 1000000000

"""