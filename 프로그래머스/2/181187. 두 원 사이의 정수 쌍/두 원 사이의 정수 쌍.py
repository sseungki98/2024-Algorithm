import math
def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        x_1 = 0
        if i > r1:
            x_1 = 0
        else:
            x_1 = math.sqrt(r1 ** 2 - i ** 2)
        x_2 = math.sqrt(r2 ** 2 - i ** 2)

        answer += int(math.floor(x_2) - math.ceil(x_1)+1)

    answer *= 4

    
    return answer