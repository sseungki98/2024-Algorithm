word_1 = input()
word_2 = input()
word_3 = input()

l_1 = len(word_1)
l_2 = len(word_2)
l_3 = len(word_3)

dp = [[[0] * (l_3 + 1) for _ in range(l_2 + 1)] for _ in range(l_1 + 1)]

for i in range(1, l_1+1):
    for j in range(1, l_2+1):
        for k in range(1, l_3+1):
            if word_1[i-1] == word_2[j-1] and word_2[j-1] == word_3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])

ans = 0
for item_1 in dp:
    for item_2 in item_1:
        for item_3 in item_2:
            ans = max(item_3, ans)

print(ans)