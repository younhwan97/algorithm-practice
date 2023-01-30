import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, distance, start):
    distance[start] = 0

    que = deque()
    que.append(start)

    while que:
        a = que.popleft()

        for v, d in graph[a]:
            if distance[v] == -1:
                distance[v] = distance[a] + d
                que.append(v)
            else:
                if distance[v] > distance[a] + d:
                    distance[v] = distance[a] + d
                    que.append(v)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    start, end, distance = map(int, input().split())
    start, end = start - 1, end - 1
    graph[start].append((end, distance))
    graph[end].append((start, distance))

distance = [-1] * N
bfs(graph, distance, 0)
print(distance[N - 1])