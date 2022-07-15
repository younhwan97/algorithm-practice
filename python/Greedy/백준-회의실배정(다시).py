import sys, heapq

N = int(sys.stdin.readline())
arr = list()
scheduler = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    arr.append((start, end))

arr.sort()

for i in range(0, len(arr)):
    if scheduler:
        temp = heapq.heappop(scheduler)
        start = -1 * temp[0]
        end = -1 * temp[1]

        if end <= arr[i][0]:
            heapq.heappush(scheduler, temp)
            heapq.heappush(scheduler, (-1 * arr[i][0], -1 * arr[i][1]))
        else:
            if end > arr[i][1]:
                heapq.heappush(scheduler, (-1 * arr[i][0], -1 * arr[i][1]))
            else:
                heapq.heappush(scheduler, temp)
    else:
        heapq.heappush(scheduler, (-1 * arr[0][0], -1 * arr[0][1]))

print(len(scheduler))