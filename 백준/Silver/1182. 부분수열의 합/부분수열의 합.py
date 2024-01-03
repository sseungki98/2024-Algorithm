from itertools import combinations

N, S = map(int, input().split())
target = list(map(int, input().split()))

count = 0
for i in range(N):
    combi = list(combinations(target, i + 1))
    for item in combi:
        if sum(item) == S:
            count += 1

print(count)
