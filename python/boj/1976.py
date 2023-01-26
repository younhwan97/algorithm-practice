import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(graph, connected, visited, start, now):
    visited[now] = True

    for v in graph[now]:
        if not visited[v]:
            connected[start][v] = True
            connected[v][start] = True
            dfs(graph, connected, visited, start, v)

n = int(input())
k = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            graph[i].append(j)

root = list(map(int, input().split()))
for i in range(k): root[i] -= 1

connected = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            connected[i][j] = True
            break

for i in range(n):
    visited = [False] * n
    dfs(graph, connected, visited, i, i)

ans = "YES"
for i in range(1, k):
    start = root[i - 1]
    end = root[i]

    if not connected[start][end]:
        ans = "NO"
        break

print(ans)
