import sys, heapq

N = int(sys.stdin.readline())
arr = list()
pq = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    arr.append((start, end))

arr.sort()

for i in range(0, len(arr)):
    if pq:
        temp = heapq.heappop(pq)

        if temp <= arr[i][0]:
            heapq.heappush(pq, temp)
            heapq.heappush(pq, arr[i][1])
        else:
            heapq.heappush(pq, temp)
    else:
        heapq.heappush(pq, arr[i][1])

print(pq)