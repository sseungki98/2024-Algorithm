from collections import deque
n = int(input())
target = deque()
for _ in range(n):
    target.append(int(input()))

stack = []
answer = []
for i in range(1, n+1):
    if i < target[0]:
        stack.append(i)
        answer.append('+')
        continue

    if i == target[0]:
        answer.append('+')
        answer.append('-')
        target.popleft()
        while stack and stack[-1] >= target[0]:
            if stack[-1] == target[0]:
                stack.pop()
                target.popleft()
                answer.append('-')
            elif stack[-1] > target[0]:
                stack.pop()
                answer.append('-')

if len(target) == 0:
    for i in answer:
        print(i)
else:
    print('NO')




