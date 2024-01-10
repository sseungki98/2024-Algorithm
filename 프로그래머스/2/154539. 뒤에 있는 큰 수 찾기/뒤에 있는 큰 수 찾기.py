def solution(numbers):
    length = len(numbers)
    answer = [-1] * length
    stack = []
    for i in range(length):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer