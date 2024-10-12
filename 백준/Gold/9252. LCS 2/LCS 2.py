word1 = list(input())
word2 = list(input())

l1, l2 = len(word1), len(word2)
store = []
for _ in range(l2):
    store.append([0, ""])


for i in range(l1):
    word = ""
    cnt = 0
    for j in range(l2):
        if cnt < store[j][0]:
            word = store[j][1]
            cnt = store[j][0]
        elif word1[i] == word2[j]:
                word += word1[i]
                store[j][1] = word
                store[j][0] = cnt + 1

store = sorted(store, key = lambda x:-x[0])
if store[0][0] == 0:
    print(store[0][0])
else:
    print(store[0][0])
    print(store[0][1])