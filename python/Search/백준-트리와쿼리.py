import sys

## 입력
N, R, Q = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

query = []
for _ in range(Q): query.append(int(sys.stdin.readline()))

## 탐색 메서드 정의
def search(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            if i < v:
                resukt[i] = resukt[v] - 1

## 탐색
resukt = [0] * (N + 1)
result[R] = N

visited = [False] * (N + 1)
search(R)