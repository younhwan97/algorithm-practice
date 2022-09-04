import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

graph = []
for _ in range(n): graph.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def seach(x, y):
    global cnt

    visited[x][y] = True

    if graph[x][y] == "P":
        cnt += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if not visited[nx][ny] and graph[nx][ny] != "X":
                seach(nx, ny)

visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            seach(i, j)
            break

if cnt == 0:
    print("TT")
else:
    print(cnt)