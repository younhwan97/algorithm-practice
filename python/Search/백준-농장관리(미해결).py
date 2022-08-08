import sys

## 입력 및 그래프 생성
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N): graph.append(list(map(int, input().split())))

## 탐색 메서드 정의
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def search(x, y):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if not visited[nx][ny] and abs(graph[nx][ny] - graph[x][y]) <= 1 and graph[nx][ny] != 0:
                search(nx, ny)

## 탐색
visited = [[False] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] != 0:
            cnt += 1
            search(i, j)

print(cnt)
