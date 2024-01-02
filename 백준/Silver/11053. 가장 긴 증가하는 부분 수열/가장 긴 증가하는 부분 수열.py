N = int(input())
target = list(map(int, input().split()))
dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if target[i] > target[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
