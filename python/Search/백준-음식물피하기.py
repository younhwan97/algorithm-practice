import sys
from collections import deque

## 입력 및 그래프 생성
N, M, K = map(int, sys.stdin.readline().split())

graph = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1

## 탐색 메서드 정의
def search(x, y):
    visited[x][y] = True

    ## 큐 정의
    que = deque()
    que.append((x, y))

    ## 인접 영역의 개수
    cnt = 1

    ## 반복
    while que:
        a, b = que.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    cnt += 1
                    que.append((nx, ny))
    
    return cnt

## 탐색
visited = [[False] * M for _ in range(N)]
max_area = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            area = search(i, j)

            if area > max_area:
                max_area = area

print(max_area)