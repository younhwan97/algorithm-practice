from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, distance, N, M):
    distance[0][0] = 1

    que = deque()
    que.append((0, 0))

    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 0:
                    if distance[nx][ny] == -1:
                        distance[nx][ny] = distance[a][b] + 1
                        que.append((nx, ny))
                    else:
                        if distance[a][b] + 1 < distance[nx][ny]:
                            distance[nx][ny] = distance[a][b] + 1
                            que.append((nx, ny))

def solve():
    N, M = map(int, input().split())

    graph = []

    for _ in range(N):
        tmp = list(map(int, list(input().strip())))
        graph.append(tmp)

    ans = N * M + 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                graph[i][j] = 0

                distance = [[-1] * M for _ in range(N)]
 
                bfs(graph, distance, N, M)

                if distance[N - 1][M - 1] != -1:
                    ans = min(ans, distance[N - 1][M - 1])

                graph[i][j] = 1

    if ans == M * N + 1:
        print(-1)
    else:
        print(ans)

solve()