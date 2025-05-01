from collections import defaultdict
def solution(tickets):
    answer = []
    t_dict = defaultdict(list)
    
    for tks in tickets:
        t_dict[tks[0]].append([tks[1], False])  
    
    for key in t_dict.keys():
        t_dict[key].sort(key = lambda x:x[0])
    
    def dfs(start, route, used_count):
        nonlocal answer
        route.append(start)
        if used_count == len(tickets):
            answer = route.copy()

            return True
        
        for dest in t_dict[start]:
            if dest[1] == False:
                dest[1] = True
                if dfs(dest[0], route, used_count + 1):
                    return True
                else:
                    dest[1] = False
        route.pop()
    dfs("ICN", [], 0)
    return answer