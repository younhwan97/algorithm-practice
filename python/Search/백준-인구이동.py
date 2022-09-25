import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

sum = 0
cnt = 0
def search(x, y, N, M, graph, visited, check, left, right):
    global sum
    global cnt

    visited[x][y] = True
    check[x][y] = True

    sum += graph[x][y]
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if not visited[nx][ny] and (left <= abs(graph[nx][ny] - graph[x][y]) <= right):
                search(nx, ny, N, M, graph, visited, check, left, right)

def can_search(x, y, N, M, graph, left, right):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M) and (left <= abs(graph[nx][ny] - graph[x][y]) <= right):
            return True
    return False

def solution():
    global sum
    global cnt

    n, l, r = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    finish_loof = False
    day = 0
    while True:
        if finish_loof:
            break
        
        day += 1
        visited = [[False] * n for _ in range(n)]    

        finish_loof = True
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and can_search(i, j, n, n, graph, l, r):
                    check = [[False] * n for _ in range(n)]
                    sum = 0
                    cnt = 0
                    finish_loof = False

                    search(i, j, n, n, graph, visited, check, l, r)

                    for k in range(n):
                        for t in range(n):
                            if check[k][t]:
                                graph[k][t] = int(sum / cnt)
                    
    return day - 1

print(solution())