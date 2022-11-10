import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m, x, y, graph, distance, visited):
    visited[x][y] = True

    que = deque()
    que.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < m) and (0 <= ny < n):
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        distance[nx][ny] = 0
                        visited[nx][ny] = True
                        que.append((nx, ny))
                    elif graph[nx][ny] == 0:
                        if distance[nx][ny] > distance[a][b] + 1:
                            distance[nx][ny] = distance[a][b] + 1
                            visited[nx][ny] = True
                            que.append((nx, ny))
                else:
                    if distance[nx][ny] > distance[a][b] + 1:
                        distance[nx][ny] = distance[a][b] + 1
                        que.append((nx, ny))

def solve():
    # 입력
    n, m = map(int, input().split())

    graph = []
    for _ in range(m): graph.append(list(map(int, input().split())))

    # 탐색
    distance = [[1000000] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if graph[i][j] == -1:
                distance[i][j] = -1
            elif graph[i][j] == 1:
                distance[i][j] = 0

    for i in range(m):
        finish_loof = False
        for j in range(n):
            if graph[i][j] == 1:
                distance[i][j] = 0
                bfs(n, m, i, j, graph, distance,visited)   
                finish_loof = True
                break
        if finish_loof:
            break

    # 결과
    if max(map(max, distance)) == 1000000:
        print(-1)
    else:
        print(max(map(max, distance)))
        
solve()