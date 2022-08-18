import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque()
def search():
    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] == 0 and graph[nx][ny] > graph[a][b] + 1:
                    graph[nx][ny] = graph[a][b] + 1
                    que.append((nx, ny))
                    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i, j))
            search()

has_zero = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            has_zero = True
            break
    if has_zero:
        break

if has_zero:
    print(-1)
else:
    print(max(map(max, graph)) - 1)