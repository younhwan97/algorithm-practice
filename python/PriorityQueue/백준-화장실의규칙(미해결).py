import sys, heapq

N, M, K = map(int, sys.stdin.readline().split())

group = 0
number = 0
line = 1

pq = [[] for _ in range(M)]

for i in range(N):
    day, hard = map(int, sys.stdin.readline().split())

    if number == K:
        heapq.heappush(pq[group % M], (line, -1 * day, -1 * hard, 'target'))
    else:
        heapq.heappush(pq[group % M], (line, -1 * day, -1 * hard, 'non_target'))
    number += 1
    group += 1

    if i != 0 and group % M == 0:
        line += 1

cnt = 0
finish_loof = False

temp = []
index = 0
while pq:
    temp = heapq.heappop(pq[index % M])
    index += 1

    heapq.heappush(temp, (temp[0], temp[1], temp[2], temp[3]))

    