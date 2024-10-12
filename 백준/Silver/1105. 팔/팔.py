L, R = map(int, input().split())

L_size = len(str(L))
R_size = len(str(R))

if L_size != R_size:
    print(0)
else:
    count = 0
    L_str = str(L)
    R_str = str(R)
    for i in range(L_size):
        if L_str[i] == R_str[i]:
            if L_str[i] == '8':
                count += 1
        else:
            break

    print(count)
