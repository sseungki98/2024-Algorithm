def solution(cap, n, deliveries, pickups):
    answer = 0
    dist = 0
    objects = [0 for _ in range(n)]
    save = n-1
    p_idx = -1
    d_idx = -1
    
    while deliveries or pickups:
        d_cap, p_cap = cap, cap
        
        if deliveries:
            while deliveries and deliveries[-1] == 0:
                deliveries.pop()
        
        if pickups:
            while pickups and pickups[-1] == 0:
                pickups.pop()
        
        if not deliveries and not pickups:
            break
        
        dist += max(len(deliveries), len(pickups)) * 2
        

        while deliveries:
            if deliveries[-1] <= d_cap:
                d_cap -= deliveries.pop()
            else:
                deliveries[-1] -= d_cap
                break


        while pickups:
            if pickups[-1] <= p_cap:
                p_cap -= pickups.pop()
            else:
                pickups[-1] -= p_cap
                break
                        
                                 
    return dist