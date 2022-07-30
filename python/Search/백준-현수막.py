import sys
from collections import deque

## 입력 및 그래프 생성
M, N = map(int, sys.stdin.readline().split())

graph = []
for _ in range(M): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
def search(x, y):
    graph[x][y] = -1

    ## 큐 생성
    que = deque()
    que.append((x, y))

    ## 반복
    while que:
        a, b = que.popleft()

        ## 탐색 방향 정의
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]

        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < M) and (0 <= ny < N):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = -1
                    que.append((nx, ny))

## 탐색
cnt = 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            search(i, j)

print(cnt)