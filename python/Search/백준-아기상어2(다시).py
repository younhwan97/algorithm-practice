import sys
from collections import deque

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 함수 정의
def search(x, y):
    distance[x][y] = 0
    visited[x][y] = True

    que = deque()
    que.append((x, y))

    while que:
        a, b = que.popleft()

        ## 8방향 이동
        dx = [1, -1, 0, 0, 1, -1, 1, -1]
        dy = [0, 0, 1, -1, 1, 1, -1, -1]

        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    temp = distance[a][b] + 1

                    if temp < distance[nx][ny] or distance[nx][ny] == -1:
                        distance[nx][ny] = temp

                    visited[nx][ny] = True
                    que.append((nx, ny))

## 탐색
distance = [[-1] * M for _ in range(N)]
visited = [[False] * (M) for _ in range(N)]  

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            search(i, j)
            visited = [[False] * (M) for _ in range(N)]  

print(max(map(max, distance)))