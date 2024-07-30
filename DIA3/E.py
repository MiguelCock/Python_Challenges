t = int(input())

nums = []
for i in range(t):
	A, B = input().split(" ")
	A = int(A)
	B = int(B)
	if A < B:
		print('No')
	else:
		res = A - B
		if res % 2 == 0:
			print("yes")
		else:
			print("no")