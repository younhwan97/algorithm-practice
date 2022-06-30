import sys
sys.setrecursionlimit(10**6)

def search(graph, x, y, M, N):
    global answer

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N):
            if graph[nx][ny] ==  0:
                search(graph, nx, ny, M, N)
                answer -= 1

M, N, K = map(int, input().split())

graph = [[0] * (M) for _ in range(N)]

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())

    for i in range(a, c):
        for j in range(b, d):
            graph[i][j] = 1

answer = M * N
search(graph, 0, 0, M, N)
print(answer)