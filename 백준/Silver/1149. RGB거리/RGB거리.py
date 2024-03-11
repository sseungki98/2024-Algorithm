N = int(input())
prices = []
dp = [[1000, 1000, 1000] for _ in range(N)]
for i in range(N):
    price = list(map(int, input().split()))
    prices.append(price)

dp[0] = prices[0]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1] + prices[i][0], dp[i-1][2] + prices[i][0])
    dp[i][1] = min(dp[i - 1][2] + prices[i][1], dp[i - 1][0] + prices[i][1])
    dp[i][2] = min(dp[i - 1][1] + prices[i][2], dp[i - 1][0] + prices[i][2])

print(min(dp[N-1]))