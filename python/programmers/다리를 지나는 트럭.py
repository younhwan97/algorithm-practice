from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    que = deque()
    que.append((truck_weights[0], 1))
    answer += 1
    idx = 1
    time = 1
    while que:
        first_weight, move = que[0]
        total_weight = 0
        time += 1
        
        if move == bridge_length:
            que.popleft()
        
        for i in range(len(que)):
            que[i] = (que[i][0], que[i][1] + 1)
            total_weight += que[i][0]
            
        if idx < len(truck_weights) and total_weight + truck_weights[idx] <= weight:
            que.append((truck_weights[idx], 1))
            idx += 1
    answer = time
    return answer