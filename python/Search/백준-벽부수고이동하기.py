import sys
from collections import deque

def search(x, y, X, Y, graph, visited, distance):
    visited[x][y] = True

    que = deque()
    que.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        a, b = que.popleft()
        length, cnt = distance[a][b]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < X) and (0 <= ny < Y):
                if not visited[nx][ny] and graph[nx][ny] == "0":
                    visited[nx][ny] = True
                    distance[nx][ny] = (length + 1, cnt)
                    que.append((nx, ny))
                elif not visited[nx][ny] and graph[nx][ny] == "1":
                    visited[nx][ny] = True
                    
                    if cnt == 0:
                        distance[nx][ny] = (length + 1, 1)
                        que.append((nx, ny))

    return distance[X - 1][Y - 1][0]
 
def soultion():
    n, m = map(int, input().split())

    graph = []

    for _ in range(n):
        tmp = list(input().strip())
        graph.append(tmp)

    visited = [[False] * m for _ in range(n)]
    distance = [[(0, 0)] * m for _ in range(n)]
    distance[0][0] = (1, 0)

    ans = search(0, 0, n, m, graph, visited, distance)
    print(distance)
    if ans == 0:
        print(-1)
    else:
        print(ans)

soultion()