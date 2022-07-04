from queue import PriorityQueue

n, m = map(int, input().split())

temp = list(map(int, input().split()))
pq = PriorityQueue()

for i in range(0, len(temp)):
    pq.put(temp[i])

for i in range(m):
    a = pq.get()
    b = pq.get()

    pq.put(a + b)
    pq.put(a + b)

answer = 0

while True:
    if pq.qsize() == 0:
        print(answer)   
        break
    else:
        answer += pq.get()