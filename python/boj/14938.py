import sys, heapq
input = sys.stdin.readline

N, M, R = map(int, input().split())
cnt = list(map(int, input().split()))
cnt = [0] + cnt
graph = [[] for _ in range(N + 1)]

INF = 100000000

for _ in range(R):
    s, e, p = map(int, input().split())
    graph[s].append((e, p))
    graph[e].append((s, p))

def dijkstra(start, distance):
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, current = heapq.heappop(pq)

        if dist > distance[current]: continue
        for v, cost in graph[current]:
            if cost + dist < distance[v]:
                distance[v] = cost + dist
                heapq.heappush(pq, (cost + dist, v))

ans = 0
for start in range(1, N + 1):
    distance = [INF] * (N + 1)
    dijkstra(start, distance)
    tmp = 0
    for i in range(1, N + 1):
        if distance[i] <= M:
            tmp += cnt[i]
    ans = max(ans, tmp)

print(ans)