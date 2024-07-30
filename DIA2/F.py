_ = input()
nums: list = sorted(list(map(int, input().split())), reverse=True)

min1: int = 0
min2: int = 0

lenn: int = len(nums) - 3
pos = 0

while pos != lenn or lenn == 0:
    if lenn == 3:
        lenn+=1
    max: int = nums[pos]
    for num in nums[pos+1:]:
        if num > min1:
            min2 = min1
            min1 = num
        elif num > min2:
            min2 = num
        if min1 + min2 > max:
            print('YES')
            exit()
    pos += 1
print('NO')
