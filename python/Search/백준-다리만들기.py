import sys
from collections import deque

##  입력
n = int(sys.stdin.readline())

graph = []
for _ in range(n): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색 메서드 정의
#### 같은 대륙의 번호를 변경하는 탐색 메서드
def search(x, y, index):
    visited[x][y] = True

    graph[x][y] = index

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny] and graph[nx][ny] == 1:
                search(nx, ny, index)


def search2(x, y):
    visited[x][y] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny] and graph[nx][ny] == 1:
                search2(nx, ny, index)


## 탐색
visited = [[False] * n for _ in range(n)]

index = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            search(i, j, index)
            index += 1
    
visited = [[False] * n for _ in range(n)]