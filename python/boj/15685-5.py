import sys
input = sys.stdin.readline

N = int(input())
graph = [[0] * 101 for _ in range(101)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0] 

for _ in range(N):
    y, x, dir, gen = map(int, input().split())
    graph[x][y] = 1

    curve = [dir]

    for i in range(gen):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)
    
    for i in range(len(curve)):
        x = x + dx[curve[i]]
        y = y + dy[curve[i]]

        if (0 <= x < 101) and (0 <= y < 101):
            graph[x][y] = 1
    
ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i + 1][j + 1] == 1 and graph[i][j + 1] == 1:
            ans += 1

print(ans)