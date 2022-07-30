import sys
from collections import deque

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): graph.append(list(sys.stdin.readline().strip()))

## 탐색 메서드 정의
def search(x, y):
    ## 늑대와 양의 마릿수
    wolf = 0
    sheep = 0

    if graph[x][y] == 'v':
        wolf += 1
    elif graph[x][y] == 'k':
        sheep += 1

    ## 방문 처리
    graph[x][y] = -1

    ## 큐 생성
    que = deque()
    que.append((x, y))

    ## 너비 우선 탐색
    while que:
        a, b = que.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] != '#' and graph[nx][ny] != -1:
                    que.append((nx, ny))
                    
                    if graph[nx][ny] == 'v':
                        wolf += 1
                    elif graph[nx][ny] == 'k':
                        sheep += 1
                    
                    graph[nx][ny] = -1
    
    if wolf == 0 and sheep == 0:
        return 0, 0
    else:
        if wolf >= sheep:
            return 1, wolf
        else:
            return -1, sheep
    
## 탐색
wolf_cnt = 0
sheep_cnt = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] != '#' and graph[i][j] != -1:
            value, cnt = search(i, j)
     
            if value == 1:
                wolf_cnt += cnt
            elif value == -1:
                sheep_cnt += cnt

print(sheep_cnt, wolf_cnt)