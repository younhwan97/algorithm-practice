import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(M):
    graph.append(list(input().strip()))

## 탐색 메서드 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y, color):
    global temp_white
    global temp_blue

    if color == 'W':
        temp_white += 1
    else:
        temp_blue += 1

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N):
            if not visited[nx][ny] and color == graph[nx][ny]:
                search(nx, ny, color)

white = 0
blue = 0
visited = [[False] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                temp_white = 0
                search(i, j, 'W')
                white += (temp_white * temp_white)
            elif graph[i][j] == 'B':
                temp_blue = 0
                search(i, j, 'B')
                blue += (temp_blue * temp_blue)
            
print(white, blue)