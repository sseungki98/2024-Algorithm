N, D = map(int, input().split())
dp = [i for i in range(10001)]
answer_list = []
store = []
for _ in range(N):
    store.append(list(map(int, input().split())))

store = sorted(store, key=lambda x:-x[0])

for _ in range(N):
    start, end, length = store.pop()

    if (end-start) > length:
        temp = 10001
        if start > 0:
            for j in range(1, start+1):
                if temp > (start - j + dp[j]):
                    temp = start - j + dp[j]
            dp[start] = temp
        dp[end] = min(dp[start] + length, dp[end])

for i in range(len(dp[:D+1])):
    answer_list.append(dp[i] + (D-i))


print(min(answer_list))

