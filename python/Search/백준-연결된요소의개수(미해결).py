def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, k = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] * n for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0

dfs(graph, 1, )