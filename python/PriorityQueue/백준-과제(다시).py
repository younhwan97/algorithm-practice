import sys, heapq

N = int(sys.stdin.readline())
pq = []
day_max = 0

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())

    heapq.heappush(pq, (-1 * w, -1 * d))

    if d > day_max:
        day_max = d

arr = [0] * (day_max + 1)

while pq:
    temp = heapq.heappop(pq)
    score = -1 * temp[0]
    day = -1 * temp[1]

    if arr[day] == 0:
        arr[day] = score
    else:
        for i in range(0, day):
            if day - i - 1 > 0 and arr[day - i - 1] == 0:
                arr[day - i  - 1] = score
                break

print(sum(arr))