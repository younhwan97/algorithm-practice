import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, distance, start):
    distance[start] = 0

    que = deque()
    que.append(start)

    while que:
        v = que.popleft()

        for nv, weight in graph[v]:
            if distance[nv] == -1:
                distance[nv] = distance[v] + weight
                que.append(nv)
            else:
                if distance[nv] > distance[v] + weight:
                    distance[nv] = distance[v] + weight
                    que.append(nv)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

btoa = [-1] * (N + 1)
bfs(graph, btoa, X)

ans = -1
for v in range(1, N + 1):
    if v != X:
        atob = [-1] * (N + 1)
        bfs(graph, atob, v)
        ans = max(ans, atob[X] + btoa[v])

print(ans)