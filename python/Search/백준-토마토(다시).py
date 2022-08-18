import sys, copy
from collections import deque

## 입력 및 그래프 생성
input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[] for _ in range(h)]

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

## 탐색 메서드 정의
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def search(x, y, f):
    que = deque()
    que.append((x, y, f))

    while que:
        a, b, c = que.popleft()

        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]

            if (0 <= nx < n) and (0 <= ny < m) and (0 <= nz < h):
                if graph[nz][nx][ny] == 0 or graph[nz][nx][ny] > graph[c][a][b] + 1:
                    graph[nz][nx][ny] = graph[c][a][b] + 1
                    que.append((nx, ny, nz))
                        
## 탐색
has_zero = False

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                has_zero = True
                break
        if has_zero:
            break
    if has_zero:
        break

if not has_zero:
    ## 모두 익어있는 경우
    print(0)
else:
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 1:
                    search(i, j, k)
    
    has_zero = False
    max_value = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 0:
                    has_zero = True
                if max_value < graph[k][i][j]:
                    max_value = graph[k][i][j]

    if has_zero:
        print(-1)
    else:
        print(max_value - 1)