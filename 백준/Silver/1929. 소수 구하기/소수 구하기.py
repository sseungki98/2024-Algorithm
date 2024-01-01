M, N = map(int, input().split())
# 두 수 사이의 소수 출력하기
memo = [False] * (N+1)

def arasto(n):
    end_num = int(n ** (1/2))
    for j in range(2, end_num+1):
        if n % j == 0:
            return False
    memo[n] = True
    return True


for i in range(M, N+1):
    arasto(i)

memo[1] = False
for i in range(len(memo)):
    if memo[i]:
        print(i)
