import sys, heapq

N = int(input())
pq = []

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))

    if temp[0] == 0:
        if len(pq) == 0:
            print(-1)
        else:
            value = heapq.heappop(pq)
            print(-1 * value)
    else:
        for i in range(1, len(temp)):
            heapq.heappush(pq, -1 * temp[i])