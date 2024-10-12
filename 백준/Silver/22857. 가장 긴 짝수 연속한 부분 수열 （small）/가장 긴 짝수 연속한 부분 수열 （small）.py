from bisect import bisect_left
N, K = map(int, input().split())
stack = list(map(int, input().split()))

head = 0
tail = 0
hol_cnt = 0
answer = 0

while True:
    if hol_cnt > K:
        if stack[tail] % 2 == 1:
            hol_cnt -= 1
        tail += 1
    elif head == N:
        break
    else:
        if stack[head] % 2 == 1:
            hol_cnt += 1
        head += 1

    if hol_cnt <= K:
        answer = max(answer, head - tail - hol_cnt)

print(answer)