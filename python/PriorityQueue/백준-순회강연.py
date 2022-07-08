import sys, heapq

N = int(sys.stdin.readline())
pq = []

day_max = 0

for _ in range(N):
    p, d = map(int, sys.stdin.readline().split())

    heapq.heappush(pq, (-1 * p, -1 * d))

    if day_max < d:
        day_max = d

schedule = [0] * (day_max + 1)

while pq:
    temp = heapq.heappop(pq)
    pay = -1 * temp[0]
    day = -1 * temp[1]

    if schedule[day] == 0:
        schedule[day] = pay
    else:
        for i in range(0, day):
            if schedule[day - i - 1] == 0 and day - i - 1 > 0:
                schedule[day - i -1] = pay
                break

print(sum(schedule))