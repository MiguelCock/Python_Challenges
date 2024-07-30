t = int(input())

for _ in range(t):
	A, B = input().split()
	A = int(A)
	B = int(B)

	print(min((A+B)//4, A, B))