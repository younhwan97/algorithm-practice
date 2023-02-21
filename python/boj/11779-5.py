import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 1000000000
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, p = map(int, input().split())
    graph[s].append((e, p))

start, end = map(int, input().split())
distance = [INF] * (N + 1)
ans = []

def dijkstra(start):
    global ans

    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start, [start]))

    while pq:
        dist, current, root = heapq.heappop(pq)
        
        if dist > distance[current]: continue
        for v, d in graph[current]:
            if d + dist < distance[v]:
                distance[v] = d + dist

                new_root = root.copy()
                new_root.append(v)

                if v == end:
                    ans = new_root.copy()

                heapq.heappush(pq, (distance[v], v, new_root))

dijkstra(start)
print(distance[end])
print(len(ans))

for i in ans:
    print(i, end = " ")