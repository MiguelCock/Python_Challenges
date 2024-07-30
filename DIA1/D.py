people = int(input())

money = list(map(int, input().split()))
maxx = max(money)

sum = 0
for val in money:
	sum += maxx - val

print(sum)