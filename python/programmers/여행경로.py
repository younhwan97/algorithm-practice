answer = []

def dfs(now, tickets, visited, path):
    global answer
    
    check = True
    for i in visited:
        if not i:
            check = False
            break
    
    if check:
        if not answer:
            answer = path.copy()
        else:
            if "".join(answer) > "".join(path):
                answer = path.copy()
    
    for i in range(len(tickets)):
        if not visited[i]:
            if tickets[i][0] == now:
                new_visited = visited.copy()
                new_visited[i] = True
                new_path = path.copy()
                new_path.append(tickets[i][1])
                dfs(tickets[i][1], tickets, new_visited, new_path)
    
def solution(tickets):
    global answer
    visited = [False] * (len(tickets))
    path = ["ICN"]
    dfs("ICN", tickets, visited, path)
    return answer