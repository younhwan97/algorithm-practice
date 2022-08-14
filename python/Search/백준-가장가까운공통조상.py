import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def search(v, e):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            search(i, e)

t = int(input())

for _ in range(t):
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())

    visited = [False] * (n + 1)
    search(start, end)