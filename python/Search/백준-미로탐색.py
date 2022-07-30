import sys
from collections import deque

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    temp = list(sys.stdin.readline().strip())
    temp = list(map(int, temp))
    graph.append(temp)

## 탐색 메서드 정의
def search(start_x, start_y):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    # 큐 생성
    que = deque()
    que.append((start_x, start_y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx, ny))
    return graph[N - 1][M -  1]

## 탐색
print(search(0, 0))