import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
def search(x, y):
    ## 방문 처리
    visited[x][y] = True

    ## 큐 생성
    que = deque()
    que.append((x, y))

    ## 반복
    while que:
        a, b = que.popleft()

        ## 탐색 방향 정의
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        sea_cnt = 0
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if not visited[nx][ny]:
                    if graph[nx][ny] > 0:
                        visited[nx][ny] = True
                        que.append((nx, ny))
                    else:
                        sea_cnt += 1
        
        if graph[a][b] >= sea_cnt:
            graph[a][b] -= sea_cnt
        else:
            graph[a][b] = 0

## 빙산의 개수를 카운트 하는 탐색 메서드 정의
def search2(x, y):
    visited[x][y] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = True
                search(nx, ny)

## 탐색
visited = [[False] * M for _ in range(N)]
year = 0
while True:
    year += 1

    cnt = 0 
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                cnt += 1
                search(i, j)
    
    ## 빙산이 모두 녹았는지 확인
    finish_loof = True
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                finish_loof = False
                break
        if not finish_loof:
            break
    
    if cnt >= 2:
        if finish_loof:
            print(0)
        else:
            print(year - 1)
        break
    else:
        visited = [[False] * M for _ in range(N)]

        if finish_loof:
            print(0)
            break