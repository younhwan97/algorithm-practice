import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def search(num):
    visited[num] = True

    for v in graph[num]:
        if not visited[v]:
            parent[v] = num
            search(v)  

visited = [False] * (n + 1)
parent = [0] * (n + 1)
search(1)

for i in range(2, len(parent)):
    print(parent[i])