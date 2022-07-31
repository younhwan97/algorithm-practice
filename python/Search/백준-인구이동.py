import sys
from collections import deque

## 입력 및 그래프 생성
N, L, R = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
def search(x, y):
    global day

    ## 방문 체크
    visited[x][y] = True

    ## 큐 생성
    que = deque()
    que.append((x, y))

    ## 연합
    group = []
    group_id = []
    group.append(graph[x][y])
    group_id.append((x, y))

    ## 반복
    while que:
        a, b = que.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < N):
                if L <= abs(graph[a][b] - graph[nx][ny]) <= R:
                    if not visited[nx][ny]: 
                        visited[nx][ny] = True
                        que.append((nx, ny))
                        group.append(graph[nx][ny])
                        group_id.append((nx, ny))
    
    if len(group) == 1 or len(group) == 0:
        return -1
    else:
        day += 1
        
        ## 연합에 속한 국가 사이 인구이동을 한다.
        p = sum(group) // len(group)

        for i in range(0, len(group_id)):
            a, b = group_id[i]
            graph[a][b] = p

## 탐색
visited = [[False] * N for _ in range(N)]
day = 0
finish_loof = False

while True:
    if finish_loof:
        print(day)
        break
    else:    
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    result = search(i, j)

                    print(graph)

                    if result == -1:
                        finish_loof = True
                        break
            if finish_loof:
                break
                    
        visited = [[False] * N for _ in range(N)]
