import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def search(start):
    visited[start] = True

    que = deque()
    que.append(start)

    cnt = 1
    while que:
        v = que.popleft()

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                cnt += 1
    rel[start] = cnt


rel = [0] * (N + 1)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    search(i)

max_value = max(rel)

for i in range(len(rel)):
    if max_value == rel[i]:
        print(i, end=' ')
