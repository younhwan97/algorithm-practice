import sys
sys.setrecursionlimit(10 ** 6)

def search(v, wei):
    for i in graph[v]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            search(a, wei + b)
    
n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

## 그래프 생성.
for _ in range(n - 1):
    a, b, w = map(int, sys.stdin.readline().split())

    graph[a].append((b, w))
    graph[b].append((a, w))

## 1번 노드에서 가장 먼 곳을 구한다.
distance = [-1] * (n + 1)
distance[1] = 0
search(1, 0)

## 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
search(start, 0)

print(max(distance))