import sys, itertools
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, visited, n, m, x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                graph[nx][ny] = 2
                dfs(graph, visited, n, m, nx, ny)

def solve():
    n, m = map(int, input().split())
    graph = []

    for _ in range(n): graph.append(list(map(int, input().split())))

    can_built_wall = []

    # 벽을 세울 수 있는 공간을 구한다.
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                can_built_wall.append((i, j))

    # combination
    com = itertools.combinations(can_built_wall, 3)
    ans = 0

    # 조합 개수만큼 반복
    for c in com:
        graph_copy = []

        for j in range(n):
            graph_copy.append(graph[j].copy())

        # 벽을 세운다.
        for x, y in c:
            graph_copy[x][y] = 1

        # 바이러스를 전파한다.
        visited = [[False] * m for _ in range(n)]
        for j in range(n):
            for k in range(m):
                if graph_copy[j][k] == 2 and not visited[j][k]:
                    dfs(graph_copy, visited, n, m, j, k)

        # 안전 영역을 구한다.
        cnt = 0
        for j in range(n):
            for k in range(m):
                if graph_copy[j][k] == 0:
                    cnt += 1
        ans = max(cnt, ans)

    print(ans)

solve()