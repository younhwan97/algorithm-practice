import sys, heapq

N = int(sys.stdin.readline())

temp = list()
pq = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    temp.append((s, e))

temp.sort()

number = 1
for i in range(N):
    if len(pq) == 0:
        heapq.heappush(pq, (temp[i][1], 1, number))
        number += 1
    else:
        value = heapq.heappop(pq)
      
        if temp[i][0] > value[0]:
            heapq.heappush(pq, (temp[i][1], value[1] + 1, value[2]))
        else:
            heapq.heappush(pq, (value[0], value[1], value[2]))
            heapq.heappush(pq, (temp[i][1], 1, number))
            number += 1

answer = []

while len(pq) > 0:
    temp = heapq.heappop(pq)

    number = temp[2]
    count = temp[1]

    heapq.heappush(answer, (number, count))

print(len(answer))
while len(answer) > 0:
    if len(answer) == 1:
        print(heapq.heappop(answer)[1])
    else:
        print(heapq.heappop(answer)[1], end=" ")