import sys, heapq

N = int(input())
pq = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))

    for item in temp:
        if len(pq) < N:
            heapq.heappush(pq, item)
        else:
            value = heapq.heappop(pq)

            if value < item:
                heapq.heappush(pq, item)
            else:
                heapq.heappush(pq, value)

print(heapq.heappop(pq))