from bisect import bisect_left
N = int(input())
target = list(map(int, input().split()))
dp = 1
value = [target[0]]

for i in range(1, N):
    if target[i] > value[-1]:
        value.append(target[i])
        dp += 1
    else:
        idx = bisect_left(value, target[i])
        value[idx] = target[i]

print(dp)

