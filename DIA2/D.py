amount = input()
numbers = set(map(int, input().split()))

if len(numbers) == 1:
    print("NO")
else:
    first = second = float('inf')
    for i in numbers:
        if i < first:
            second = first
            first = i
        elif i < second:
            second = i
    print(second)