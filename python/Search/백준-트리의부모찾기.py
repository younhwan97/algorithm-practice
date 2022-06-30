import sys
sys.setrecursionlimit(10**6)

def search(graph, v, visited, parent):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            search(graph, i, visited, parent)
            parent[i] = v

N = int(input())

graph = [[]* N for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

search(graph, 1, visited, parent)

for i in range(2, len(parent)):
    print(parent[i])