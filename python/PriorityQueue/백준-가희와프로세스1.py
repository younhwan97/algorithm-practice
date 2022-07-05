import sys, heapq

T, n = map(int, sys.stdin.readline().split())

pq = []

for _ in range(n):
    id, time, priority = map(int, sys.stdin.readline().split())

    heapq.heappush(pq, (-1 * priority, id, time))

for _ in range(T):
    process = heapq.heappop(pq)

    priority = -1 * process[0] - 1
    id = process[1]
    time = process[2] - 1

    print(id)

    if time > 0:
        heapq.heappush(pq, (-1 * priority, id, time))
