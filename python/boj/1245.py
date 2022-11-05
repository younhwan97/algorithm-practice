import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def search(n, m, graph, x, y, visited):
    visited[x][y] = True
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if not visited[nx][ny] and graph[nx][ny] <= graph[x][y] and graph[nx][ny] > 0:
                search(n, m, graph, nx, ny, visited)

def solve():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n): graph.append(list(map(int, input().split())))

    visited = [[False] * m for _ in range(n)]
    cnt = 0
    while True:
        # 최대 값을 찾는다.
        max_value = -1
        x, y = -1, -1
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and graph[i][j] > max_value:
                    max_value = graph[i][j]
                    x = i
                    y = j

        if max_value == 0 or max_value == -1:
            break

        cnt += 1
        search(n, m, graph, x, y, visited)

    print(cnt)
solve()