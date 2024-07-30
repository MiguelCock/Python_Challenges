t = int(input())

for _ in range(t):
	i = int(input()) - 1
	cells = input()

	first = 0
	j = 0
	while cells[j] != 'B':
		j += 1

	while cells[i] != 'B':
		i -= 1

	print(i-j + 1)
"""
8
6
WBBWBW
1
B
2
WB
3
BBW
4
BWWB
6
BWBWWB
6
WWBBWB
9
WBWBWWWBW

"""