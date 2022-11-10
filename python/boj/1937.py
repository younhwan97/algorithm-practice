import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def update(x, y, n, graph, dp):
    updated = False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if graph[x][y] > graph[nx][ny]:     
                if dp[x][y] < dp[nx][ny] + 1:
                    dp[x][y] = dp[nx][ny] + 1
                    updated = True
    
    return updated

def find(index, n, graph, dp):
    for i in range(index):
        x = i // n
        y = i % n 

        if update(x, y, n, graph, dp):
            find(i - 1, n , graph, dp)

def solve():
    n = int(input())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dp = [[1] * n for _ in range(n)]

    find(n * n, n, graph, dp)
    
    print(max(map(max, dp)))
            
solve()