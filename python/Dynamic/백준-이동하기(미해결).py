import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

dx = [1, 1, 0]
dy = [0, 1, 1]

def search(x, y):
    visited[x][y] = True

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if not visited[nx][ny] and dp[nx][ny] < dp[x][y] + graph[nx][ny]:
                dp[nx][ny] = dp[x][y] + graph[nx][ny]
                search(nx, ny)

visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = graph[0][0]

search(0, 0)
print(dp[n-1][m-1])