import sys
input = sys.stdin.readline

# BFS는 그래프에서 간선의 가중치가 모두 같을 때의 최단 경로를 구하는 알고리즘입니다.

# DP는 부분 문제를 해결하는것으로 더 큰 문제를 해결할 수 있을 때 사용하는 알고리즘입니다.

# 위 문제는 정점 사이의 거리는 1이지만, 구하려는 답은 최단 경로가 아니므로 BFS를 적용하기 좋은 문제는 아닌 것 같습니다.

def solve():
    n, m = map(int, input().split())

    graph = [] 
    for _ in range(n): graph.append(list(map(int, input().split())))

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = graph[0][0]

    for i in range(1, m):
        dp[0][i] = dp[0][i - 1] + graph[0][i]
    
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + graph[i][0]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            dp[i][j] += graph[i][j]
    
    print(dp[n - 1][m - 1])

solve()