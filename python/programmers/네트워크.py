def dfs(visited, num, graph):
    visited[num] = True
    
    for i in range(len(graph[num])):
        if graph[num][i] == 1 and not visited[i]:
            dfs(visited, i, graph)
        
def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(visited, i, computers)
            answer += 1

    return answer