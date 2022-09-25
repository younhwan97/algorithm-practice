import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

max_value = -1 * 1_000_000_000
min_value = 1_000_000_000

def search(x, y, n, m, graph, visited, ans):
    global max_value
    global min_value

    if x == (n - 1) and y == (m - 1):
        max_value = max(max_value, eval(ans))
        min_value = min(min_value, eval(ans))
        return
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] in ("+", "-", "*"):
                    search(nx, ny, n, m, graph, visited, str(eval(ans)) + graph[nx][ny])
                else:
                    search(nx, ny, n, m, graph, visited, str(eval(ans + graph[nx][ny])))
                visited[nx][ny] = False

def solution():
    n = int(input())

    graph = []
    for _ in range(n): graph.append(list(input().split()))
    
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    search(0, 0, n, n, graph, visited, str(graph[0][0]))
    
    print(max_value, min_value)

solution()