import math
N, M = map(int, input().split())
maps = []
answers = []
for _ in range(N):
    maps.append(list(map(str, input())))

for i in range(N):
    for j in range(M):
        for k in range(-N, N):
            for m in range(-M, M):
                words = ""
                if k == 0 and m == 0:
                    continue
                x, y = i, j
                while 0 <= x < N and 0 <= y < M:
                    words += maps[x][y]
                    int_words = int(words)
                    if int(math.sqrt(int_words)) == math.sqrt(int_words):
                        answers.append(int(int_words))
                    x += k
                    y += m
if answers:
    print(max(answers))
else:
    print(-1)