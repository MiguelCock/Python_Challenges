_ = input()
nums: list = sorted(list(map(int, input().split())), reverse=True)

lenn: int = len(nums) - 3
pos: int = 0

for i in range(lenn):
	if nums[i] < nums[i + 1] + nums[i + 2]:
		print('YES')
		exit()

print('NO')
