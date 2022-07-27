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

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    index = 1

    while temp[index] != -1:
        graph[temp[0]].append((temp[index], temp[index + 1]))
        index += 2    

## 1에서 가장 먼 거리에 있는 노르들 구한다.
distance = [-1] * (n + 1)
distance[1] = 0
search(1, 0)

## 1에서 구한 노드와 가장 먼 거리에 있는 노드를 구한다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
search(start, 0)

print(max(distance))
