import sys
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
def search(x, y):
    visited[x][y] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    sea_cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] > 0:
                if not visited[nx][ny]:
                    search(nx, ny)
            elif graph[nx][ny] == 0:
                if not visited[nx][ny]:
                    sea_cnt += 1

    if graph[x][y] >= sea_cnt:
        graph[x][y] -= sea_cnt
    else:
        graph[x][y] = 0

## 탐색
year = 0
finish_infinite_loof = False
while True:
    if finish_infinite_loof:
        print(year - 1)
        break  
    else:
        year += 1

        cnt = 0
        visited = [[False] * M for _ in range(N)] 
        for i in range(N):
            for j in range(M):
                if graph[i][j] > 0 and not visited[i][j]:
                    cnt += 1
                    if cnt >= 2:
                        break
                    search(i, j)
            if cnt >= 2:
                break
    
        if cnt >= 2:
            finish_infinite_loof = True