import collections

amount = int(input())
texts = []

for _ in range(amount):
    texts.append(input().replace(" ", ""))

for text in texts:
    deque = collections.deque()
    wrong = False
    for i in text:
        if wrong:
            break
        else:
            if i == '[' or i == '(':
                deque.append(i)
            else:
                if len(deque) == 0:
                    wrong = True
                elif deque[-1] == '[' and i == ']' or deque[
                    -1] == '(' and i == ')':
                    deque.pop()
                else:
                    wrong = True
    if wrong or len(deque) != 0:
        print('No')
    else:
        print('Yes')
"""
3
([])
(([()])))
([()[]()])()
"""
