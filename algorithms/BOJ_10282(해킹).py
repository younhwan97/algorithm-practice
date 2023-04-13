import sys, heapq
input = sys.stdin.readline

def dijkstar(start, distance, graph):
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        dist, current = heapq.heappop(pq)

        if dist > distance[current]: continue
        for next, cost in graph[current]:
            if cost + dist < distance[next]:
                distance[next] = cost + dist
                heapq.heappush(pq, (cost + dist, next))

T = int(input())
INF = 1_001 * 10_000
for test_case in range(T):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(D):
        s, e, c = map(int, input().split())
        graph[e].append((s, c))

    distance = [INF] * (N + 1)
    dijkstar(C, distance, graph)

    cnt = 0
    max_value = -1
    for d in distance:
        if d != INF:
            cnt += 1
            max_value = max(max_value, d)

    print(cnt, max_value)
