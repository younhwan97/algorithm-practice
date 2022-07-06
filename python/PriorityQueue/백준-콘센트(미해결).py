import sys, heapq

N, M = map(int, sys.stdin.readline().split())
M_copy = M
arr = list(map(int, sys.stdin.readline().split()))

pq = []

for i in range(0, len(arr)):
    heapq.heappush(pq, (-1 * arr[i]))

needed_time = 0
temp = 0

while len(pq) > 0:
    charing = []

    while M > 0:
        if len(pq) != 0:
            e = -1 * heapq.heappop(pq)
            M -= 1
            charing.append(e)
        else:
            break
    
    M = M_copy

    if needed_time == 0:
        needed_time = max(charing)
        temp = max(charing[1:])
    else:
        if needed_time >= temp + max(charing):
            temp += max(charing)
        else:
            needed_time += max(charing)

print(needed_time)