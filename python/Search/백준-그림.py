from collections import deque
import sys

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
def search(x, y):
    visited[x][y] = 1

    ## 큐 생성
    que = deque()
    que.append((x, y))

    ## 인접한 영역의 개수를 카운트
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
                if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = cnt
                    que.append((nx, ny))
    
    return cnt

## 탐색
visited = [[-1] * M for _ in range(N)]
result = []

for i in range(N):
    for j in range(M):
        if visited[i][j] == -1 and graph[i][j] == 1:
            result.append(search(i, j))

if result:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)