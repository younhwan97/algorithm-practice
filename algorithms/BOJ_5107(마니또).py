import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    visited[node] = True

    for v in graph[node]:
        if not visited[v]:
            dfs(v)

tc = 1

while True:
    N = int(input())

    if N == 0: break

    graph = [[] for _ in range(N)]
    num = 0
    dic = dict()
    for _ in range(N):
        a, b = input().split()

        if a not in dic:
            dic[a] = num
            num += 1
        a = dic[a]

        if b not in dic:
            dic[b] = num
            num += 1
        b = dic[b]

        graph[a].append(b)

    visited = [False] * N
    ans = 0
    for i in range(N):
        if not visited[i]:
            ans += 1
            dfs(i)

    print(tc, ans)
    tc += 1