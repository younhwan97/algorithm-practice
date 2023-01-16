import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, visited, x, y, N):
    global cnt

    cnt += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N):
            if not visited[nx][ny] and graph[nx][ny] == '1':
                dfs(graph, visited, nx, ny, N)

N = int(input())

graph = []
for _ in range(N):
    tmp = list(input().strip())
    graph.append(tmp)

visited = [[False] * N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            cnt = 0
            dfs(graph, visited, i, j, N)
            ans.append(cnt)
ans.sort()
print(len(ans))
for num in ans:
    print(num)