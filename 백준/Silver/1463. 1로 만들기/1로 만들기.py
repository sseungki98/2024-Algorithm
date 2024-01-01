N = int(input())

count = [0] * (N+1)

for i in range(2, N+1):
    count[i] = count[i-1] + 1
    if i % 2 == 0:
        count[i] = min(count[i], count[i//2]+1)
    if i % 3 == 0:
        count[i] = min(count[i], count[i//3]+1)

print(count[N])


