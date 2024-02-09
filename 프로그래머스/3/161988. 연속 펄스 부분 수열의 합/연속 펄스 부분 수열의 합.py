def solution(sequence):
    pulse_1 = []
    pulse_2 = []
    for i in range(len(sequence)):
        if i%2 == 0:
            pulse_1.append(sequence[i])
        else:
            pulse_1.append(-sequence[i])
            
    for i in range(len(sequence)):
        if i%2 == 0:
            pulse_2.append(-sequence[i])
        else:
            pulse_2.append(sequence[i])
    dp_1 = [0 for _ in range(len(pulse_1)+1)]
    dp_2 = [0 for _ in range(len(pulse_2)+1)]
    dp_1[0] = pulse_1[0]
    dp_2[0] = pulse_2[0]
    
    # dp_1[idx]는 idx까지의 부분 수열 최대 합
    for i in range(1, len(pulse_1)):
        dp_1[i] = max(0, dp_1[i-1]) + pulse_1[i]
        dp_2[i] = max(0, dp_2[i-1]) + pulse_2[i]
    
    
    answer = max(max(dp_1), max(dp_2))
    return answer