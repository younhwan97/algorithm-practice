import sys, copy
sys.setrecursionlimit(10 ** 6)

def search(graph, visited, x, y, N, M):
    temp = graph[x][y]
    graph[x][y] = -1

    visited[x][y] = True

    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    sea_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] > 0 and visited[nx][ny] == False:
                search(graph, visited, nx, ny, N, M)
            elif graph[nx][ny] == 0:
                sea_cnt += 1

    graph[x][y] = temp

    if graph[x][y] <= sea_cnt:
        graph[x][y] = 0
    else:
        graph[x][y] -= sea_cnt


N, M = map(int, sys.stdin.readline().split())

## 그래프 초기화
graph= []
for _ in range(N): graph.append(list(map(int, sys.stdin.readline().split())))

## 방문 리스트
visited = [[False] * M for _ in range(N)]

## 결과
answer = 0
year = 1

## 탐색
graph_copy = []
for i in range(0, len(graph)):
    graph_copy.append(graph[i].copy())
    
while answer < 2:
    answer = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                search(graph, visited, i, j, N, M)
                answer += 1
             
    year += 1
    visited = [[False] * M for _ in range(N)]
    
print(year)