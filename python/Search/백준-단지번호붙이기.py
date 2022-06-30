import sys
sys.setrecursionlimit(10**6)

def search(graph, x, y, N):
    global group_cnt

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if graph[x][y] > 0:
        graph[x][y] = -1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N):
            if graph[nx][ny] > 0:
                group_cnt[len(group_cnt) -1] += 1
                search(graph, nx, ny, N)

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    row = list(input())
    row = list(map(int, row))
    graph.append(row)

group_cnt = list()

for i in range(N):
    for j in range(N):
        if graph[i][j] > 0:
            group_cnt.append(1)    
            search(graph, i, j, N)

print(len(group_cnt))

group_cnt.sort()

for i in range(0, len(group_cnt)):
    print(group_cnt[i])