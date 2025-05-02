from collections import Counter
def solution(nums):
    answer = 0
    select_count = len(nums) / 2
    counter = Counter(nums)
    c_length = len(counter)
    if select_count >= c_length:
        answer = c_length
    else:
        answer = select_count
    return answer