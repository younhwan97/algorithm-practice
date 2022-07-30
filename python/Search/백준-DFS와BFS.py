import sys
from collections import deque

## 입력 및 그래프 생성
N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a)

for i in range(0, len(graph)):
    graph[i].sort()

## dfs 정의
def search_dfs(v):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            search_dfs(i)

## bfs 정의
def search_bfs(start):
    visited[start] = True
    que = deque()
    que.append(start)

    while que:
        v = que.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


visited = [False] * (N + 1)
search_dfs(V)

print()

visited = [False] * (N + 1)
search_bfs(V)