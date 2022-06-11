import sys
sys.setrecursionlimit(10 ** 6)

def dfs(graph, v, visited):
    if visited[v] == True:
        return -1

    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
    return 0

N, M = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N + 1):
    if dfs(graph, i, visited) == 0:
        cnt += 1

print(cnt)