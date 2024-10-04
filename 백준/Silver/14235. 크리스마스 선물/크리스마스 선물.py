import heapq
n = int(input())
hq = []
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 0:
        if not hq:
            print(-1)
        else:
            print(-heapq.heappop(hq))
    else:
        for i in range(1, len(cmd)):
            heapq.heappush(hq, -cmd[i])
