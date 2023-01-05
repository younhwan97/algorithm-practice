import sys
sys.setrecursionlimit(6**8)
input = sys.stdin.readline

ans = "Yes"

def dfs(graph, visited, now, position, meet):
    global ans 

    if now in position:
        meet = True

    can_move = False
    for v in graph[now]:
        if not visited[v]:
            can_move = True

            visited[v] = True
    
            if v == 1:
                dfs(graph, visited, v, position, False)
            else:
                dfs(graph, visited, v, position, meet)

            visited[v] = False

    if not can_move and not meet:
        ans = "yes"

def solve():
    global ans

    # 입력 
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    S = int(input())
    position = set(map(int, input().split()))

    # 탐색
    visited = [False] * (N + 1)
    visited[1] = True
    dfs(graph, visited, 1, position, False)

    # 결과
    print(ans)

solve()
