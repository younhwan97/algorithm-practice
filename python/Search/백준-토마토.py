import sys, copy
from collections import deque

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(M): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
def search(x, y):
    ## 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ## 큐 생성
    que = deque()
    que.append((x, y))
    visited[x][y] = True

    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < M) and (0 <= ny < N):
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    que.append((nx, ny))
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    visited[nx][ny] = True

## 탐색
visited = [[False] * N for _ in range(M)]

finish_loof = False
old_graph = []
for i in range(0, len(graph)): old_graph.append(graph[i].copy())
day = 0
while True:
    if finish_loof:
        print(day)
        break
    else:
        day += 1

        for i in range(M):
            for j in range(N):
                if graph[i][j] == 1:
                    search(i, j)
                    break
        
        if old_graph == graph:
            finish_loof = True
        else:
            finish_loof = False
            old_graph = []
            for i in range(0, len(graph)):
                old_graph.append(graph[i].copy())
