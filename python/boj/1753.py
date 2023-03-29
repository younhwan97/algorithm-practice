import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = 1000000000
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, c = map(int, input().split())
    graph.append((e, c))

distance = [INF] * (V + 1) 

# V, E = map(int, input().split())
# K = int(input())
# INF = 1000000000
# graph = [[] for _ in range(V + 1)]
# for _ in range(E):
#     s, e, c = map(int, input().split())
#     graph[s].append((e, c))

# distance = [INF] * (V + 1)
# def dijkstra(start, distance):
#     distance[start] = 0

#     pq = []
#     heapq.heappush(pq, (0, start))

#     while pq:
#         dist, current = heapq.heappop(pq)

#         if dist > distance[current]: continue
#         for v, p in graph[current]:
#             if dist + p < distance[v]:
#                 distance[v] = dist + p
#                 heapq.heappush(pq, (dist + p, v))

# dijkstra(K, distance)
# for i in range(1, len(distance)):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

# V, E = map(int, input().split())
# K = int(input())
# graph = [[] for _ in range(V + 1)]

# for _ in range(E):
#     s, e, p = map(int, input().split())
#     graph[s].append((e, p))

# distance = [10000000000] * (V + 1)
# distance[K] = 0

# def dijk(start):
#     pq = []
#     heapq.heappush(pq, (0, start))

#     while pq:
#         p1, current = heapq.heappop(pq)

#         for v, p2 in graph[current]:
#             if p1 + p2 < distance[v]:
#                 distance[v] = p1 + p2
#                 heapq.heappush(pq, (p1 + p2, v))

# dijk(K)

# for i in range(1, V + 1):
#     if distance[i] == 10000000000:
#         print("INF")
#     else:
#         print(distance[i])