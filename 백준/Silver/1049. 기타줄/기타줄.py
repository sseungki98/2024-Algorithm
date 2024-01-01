N, M = map(int, input().split())
low_set_price = 10001
low_solo_price = 10001
for _ in range(M):
    set_price, solo_price = map(int, input().split())
    if low_set_price > set_price:
        low_set_price = set_price
    if low_solo_price > solo_price:
        low_solo_price = solo_price

quotient = (N // 6)
remain = N % 6

only_set = (quotient+1) * low_set_price
set_with_solo = quotient * low_set_price + remain * low_solo_price
only_solo = N * low_solo_price

print(min(only_set, set_with_solo, only_solo))




