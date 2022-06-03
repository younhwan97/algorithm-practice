def dfs(graph, v, visited, answer):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer += 1
            answer = dfs(graph, i, visited, answer)
    return answer

n = int(input())
k = int(input())

visited = [False] * (n + 1)

graph = [[]*n for _ in range(n+1)]

for _ in range(k):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0

print(dfs(graph, 1, visited, answer))