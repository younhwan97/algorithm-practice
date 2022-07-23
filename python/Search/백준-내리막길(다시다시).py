import sys
sys.setrecursionlimit(10**6)

def search(graph, x, y, M, N):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += search(graph, nx, ny, M, N)

    return dp[x][y]
                

M, N = map(int, sys.stdin.readline().split())

dp = [[-1] * N for _ in range(M)]

graph = []
for _ in range(M): 
    graph.append(list(map(int, sys.stdin.readline().split())))

print(search(graph, 0, 0, M, N))