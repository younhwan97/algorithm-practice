import sys
sys.setrecursionlimit(10**6)

def search(graph, x, y, M, N):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if graph[x][y] == 0:
        graph[x][y] = group_nubmer

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N):
            if graph[nx][ny] == 0:
                group[len(group) - 1] += 1
                search(graph, nx, ny, M, N)

M, N, K = map(int, sys.stdin.readline().split())

graph = [[0] * N for _ in range(M)]

group_nubmer = 1
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = group_nubmer
    
    group_nubmer += 1

group = list()
group_nubmer = 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            group_nubmer -= 1
            group.append(1)
            search(graph, i, j, M, N)

group.sort()

print(len(group))

for i in range(0, len(group)):
    print(group[i], end=" ")