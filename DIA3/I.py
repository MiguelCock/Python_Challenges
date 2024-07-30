def dfs(arr, n, m):
	x1, x2 = -1, float('inf') #up, down
	y1, y2 = -1, float('inf') #left, right

	for i in range(n):
		for j in range(m):
			if arr[i][j] == '#':
				if i > x1:
					x1 = i
				if i < x2:
					x2 = i
				if j > y1:
					y1 = j
				if j < y2:
					y2 = j

	print(x2 + (x1 - x2)//2 + 1, y2 + (y1 - y2)//2 + 1)

t = int(input())

for _ in range(t):
	nums = list(map(int, input().split()))

	grid = []
	for _ in range(nums[0]):
		grid.append(input())

	dfs(grid, nums[0], nums[1])

"""
6
5 5
.....
.....
..#..
.....
.....
5 5
..#..
.###.
#####
.###.
..#..
5 6
......
......
.#....
###...
.#....
1 1
#
5 6
...#..
..###.
.#####
..###.
...#..
2 10
..........
...#......

"""