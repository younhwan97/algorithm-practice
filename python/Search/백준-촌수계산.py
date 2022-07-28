import sys
sys.setrecursionlimit(10**6)

def search(v, e, rel):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            if distance[i] == -1:
                distance[i] = rel
            search(i, e, rel + 1)

## 입력 및 그래프 생성
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
distance = [-1] * (n + 1)
distance[a] = 0

search(a, b, 1)

print(distance[b])