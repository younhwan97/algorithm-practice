import sys
sys.setrecursionlimit(10 ** 6)
import copy

def dfs(x, y, h):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N):
            if temp_graph[nx][ny] > 0:
                temp_graph[nx][ny] = 0
                dfs(nx, ny, h)

N = int(input())
graph = []

for _ in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

max_height = 0

for i in range(N):
    if max(graph[i]) > max_height:
        max_height = max(graph[i])

max_cnt = 0
for h in range(0, max_height):
    temp_graph = []

    for i in range(N):
        temp_graph.append(graph[i].copy())

    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] <= h:
                temp_graph[i][j] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] > 0:
                dfs(i, j, h)
                cnt += 1
    
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)