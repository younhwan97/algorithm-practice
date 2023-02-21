import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, p = map(int, input().split())
    graph[s].append((e, p))

distance = [10000000000] * (V + 1)
distance[K] = 0

def dijk(start):
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        p1, current = heapq.heappop(pq)

        for v, p2 in graph[current]:
            if p1 + p2 < distance[v]:
                distance[v] = p1 + p2
                heapq.heappush(pq, (p1 + p2, v))

dijk(K)

for i in range(1, V + 1):
    if distance[i] == 10000000000:
        print("INF")
    else:
        print(distance[i])