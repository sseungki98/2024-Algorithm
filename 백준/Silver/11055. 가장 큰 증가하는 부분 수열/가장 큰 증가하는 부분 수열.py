N = int(input())
target = list(map(int, input().split()))
dp_store = [[i] for i in target]
dp = [1 for _ in range(N)]
for i in range(N):
    last_value = []
    last_sum = 0
    for j in range(i):
        if target[i] > target[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j] + 1
                if last_sum < sum(dp_store[j]):
                    last_value = dp_store[j]
                    last_sum = sum(dp_store[j])
    dp_store[i] = dp_store[i] + last_value

answer = 0
for item in dp_store:
    answer = max(answer, sum(item))


print(answer)

