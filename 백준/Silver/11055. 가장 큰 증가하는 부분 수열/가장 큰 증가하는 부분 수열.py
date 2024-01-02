N = int(input())
target = list(map(int, input().split()))
dp = [item for item in target]
for i in range(1,N):
    for j in range(i):
        if target[i] > target[j]:
            dp[i] = max(dp[i], dp[j] + target[i])
        else:
            dp[i] = max(dp[i], target[i])

print(max(dp))

