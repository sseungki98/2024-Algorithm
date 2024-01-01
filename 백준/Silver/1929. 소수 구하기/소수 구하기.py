M, N = map(int, input().split())
# 두 수 사이의 소수 출력하기
store = []

def arasto(n):
    end_num = int(n ** (1/2))
    if n == 1:
        return False
    for j in range(2, end_num+1):
        if n % j == 0:
            return False
    store.append(n)
    return True


for i in range(M, N+1):
    arasto(i)

print(*store)
