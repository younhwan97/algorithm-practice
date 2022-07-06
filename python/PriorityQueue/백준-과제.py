import sys, heapq

N = int(sys.stdin.readline())
pq = []

max = 0

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())

    if d > max:
        max = d

    heapq.heappush(pq, (-1 * w, d))

day = [0] * (max + 1) 

while len(pq) > 0:
    assign = heapq.heappop(pq)
    w = -1 * assign[0]
    d = assign[1]

    if day[d] == 0:
        day[d] = w
    else:
        print(w, d)
    
print(day)