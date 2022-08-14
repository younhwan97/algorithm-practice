import sys, copy
sys.setrecursionlimit(10000)

## 입력
input = sys.stdin.readline

N, M = map(int, input().split())

graph = list()
for _ in range(N): graph.append(list(map(int, input().split())))

## 탐색 메서드 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y):
    visited[x][y] = True

    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if not visited[nx][ny] and graph[nx][ny] > 0:
                search(nx, ny)
            elif graph[nx][ny] == 0:
                cnt += 1

    result[x][y] -= cnt
    if result[x][y] < 0:
        result[x][y] = 0
 
## 탐색
result = list()
for i in range(N): result.append(graph[i].copy())

year = 0
while True:
    year += 1
    visited = [[False] * M for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                search(i, j)
                cnt += 1

    graph = list()
    for i in range(N): graph.append(result[i].copy())

    ## 빙산이 전부 녹았는지 확인
    max_value = max(map(max, graph))
    
    if max_value == 0:
        if cnt < 2:
            print(0)
        else:
            print(year - 1)
        break
    else:
        if cnt >=2:
            print(year - 1)
            break