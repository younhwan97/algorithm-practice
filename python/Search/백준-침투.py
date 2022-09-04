import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

m, n = map(int, input().split())
graph = []

for _ in range(m):
    temp = list(input().strip())
    temp = list(map(int, temp))
    graph.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y):
    global answer

    visited[x][y] = True

    if x == m - 1:
        answer = "YES"

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < m) and (0 <= ny < n):
            if not visited[nx][ny] and graph[nx][ny] == 0:
                search(nx, ny)

visited = [[False] * n for _ in range(m)]
answer = "NO"

for i in range(n):
    if graph[0][i] == 0:
        if answer == "YES":
            print(answer)
            exit()
        else:
            search(0, i)

print(answer)