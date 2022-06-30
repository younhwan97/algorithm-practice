import sys
sys.setrecursionlimit(10**6)

def search(graph, v, visited):
    global answer
    answer += 1

    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            search(graph, i, visited)

N = int(input())
K = int(input())

graph = [[]*N for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)


answer = -1

search(graph, 1, visited)

print(answer)