import sys
from collections import deque

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): 
    temp = list(sys.stdin.readline().strip())
    graph.append(list(temp))

## 탐색 메서드 정의
def search(x, y):
    score[x][y] = 0

    ## 큐
    que = deque()
    que.append((x, y))

    while que:
        a, b = que.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 'L' and score[nx][ny] == -1:
                    score[nx][ny] = score[a][b] + 1
                    que.append((nx, ny))

    return max(map(max, score))

## 탐색
visited = [[False] * M for _ in range(N)]
score = [[-1] * M for _ in range(N)]

max_value = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            max_value = max(max_value, search(i, j))
            score = [[-1] * M for _ in range(N)]

print(max_value)