import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global distance, graph, N, M

    distance[x][y] = 0

    que = deque()
    que.append((x, y))

    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if (0 <= nx < N) and (0 <= ny < M) and graph[nx][ny] == 1:
                if distance[nx][ny] == -1:
                    distance[nx][ny] = distance[a][b] + 1
                    que.append((nx, ny))
                else:
                    if distance[nx][ny] > distance[a][b] + 1:
                        distance[nx][ny] = distance[a][b] + 1
                        que.append((nx, ny))

N, M = map(int, input().split())
graph = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

distance = [[-1] * M for _ in range(N)]
x, y = -1, -1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            x, y = i, j
            break
    if x != -1 and y != -1:
        break

bfs(x, y)
for i in range(N):
    for j in range(M):
        if distance[i][j] == -1:
            if graph[i][j] == 0:
                print(0, end = " ")
            else:
                print(-1, end = " ")
        else:
            print(distance[i][j], end= " ")
    print()