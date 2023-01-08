import sys
from collections import deque
input = sys.stdin.readline

def bfs(load, distance, x, y, N):
    distance[x][y] = 0

    que = deque()
    que.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        a, b = que.popleft()
        start = a * N + b

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < N):
                end = nx * N + ny

                if end not in load[start]:
                    if distance[nx][ny] == -1:
                        que.append((nx, ny))
                        distance[nx][ny] = distance[a][b] + 1
                    else:
                        if distance[a][b] + 1 < distance[nx][ny]:
                            distance[nx][ny] = distance[a][b] + 1
                            que.append((nx, ny))
    

def solve():
    N, K, R = map(int, input().split())
    load = [[] for _ in range(N * N)]

    for _ in range(R):
        r1, c1, r2, c2, = map(int, input().split())
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

        start = r1 * N + c1
        end = r2 * N + c2
   
        load[start].append(end)
        load[end].append(start)

    cow = []

    for _ in range(K):
        x, y = map(int, input().split())
        cow.append((x ,y))    
    
    ans = 0
    for i in range(len(cow)):
        row, col = cow[i]
        distance = [[-1] * (N) for _ in range(N)]

        bfs(load, distance, row - 1, col - 1, N)

        for j in range(i + 1, len(cow)):
            row2, col2 = cow[j]

            if distance[row2 - 1][col2 - 1] == -1:
                ans += 1

    print(ans)
    
solve()