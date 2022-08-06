import sys, copy
from collections import deque

## 입력 및 그래프 생성
N, M, F = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(F)]

for i in range(F):
    for _ in range(M):
        graph[i].append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
def search(x, y, z):
    visited[z][x][y] = 0

    ## 큐 생성
    que = deque()
    que.append((x, y, z))

    ## 반복
    while que:
        a, b, c = que.popleft()

        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0 ,0]
        dz = [0, 0, 0, 0, 1, -1]

        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]

            if (0 <= nx < M) and (0 <= ny < N) and (0 <= nz < F):
                if graph[nz][nx][ny] == 0:
                    if -2 == visited[nz][nx][ny]:
                        visited[nz][nx][ny] = visited[c][a][b] + 1
                        que.append((nx, ny, nz))
                    elif visited[nz][nx][ny] >= visited[c][a][b] + 1:
                        visited[nz][nx][ny] = visited[c][a][b] + 1
                
                print(visited)
                    
## 탐색
visited = []

for i in range(F):
    temp = [[-2] * N for _ in range(M)]
    visited.append(temp)

for i in range(M):
    for j in range(N):
        for k in range(F):
            if graph[k][i][j] == -1:
                visited[k][i][j] = -1

for i in range(M):
    for j in range(N):
        for k in range(F):
            if graph[k][i][j] == 1:
                search(i, j, k)

max_value = 0
min_value = 0

print(graph)
print(visited)

for i in range(F):
    max_value = max(max_value, max(map(max, visited[i])))
    min_value = min(min_value, min(map(min, visited[i])))

if min_value == -2:
    print(-1)
else:
    print(max_value)