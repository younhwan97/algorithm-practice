import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, change, n):
    change[0][0] = 0

    que = deque()
    que.append((0, 0))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                if graph[nx][ny] == 1:
                    # 흰 방
                    if change[nx][ny] == -1:
                        change[nx][ny] = change[a][b]
                        que.append((nx, ny))
                    else:
                        if change[nx][ny] > change[a][b]:
                            change[nx][ny] = change[a][b]
                            que.append((nx, ny))
                else:
                    # 검은 방
                    if change[nx][ny] == -1:
                        change[nx][ny] = change[a][b] + 1
                        que.append((nx, ny))
                    else:
                        if change[nx][ny] > change[a][b] + 1:
                            change[nx][ny] = change[a][b] + 1
                            que.append((nx, ny))

def solve():
    n = int(input())
    graph = []
    for _ in range(n):
        tmp = list(map(int, list(input().strip())))
        graph.append(tmp)

    change = [[-1] * n for _ in range(n)]

    bfs(graph, change, n)

    print(change[n-1][n-1])

solve()