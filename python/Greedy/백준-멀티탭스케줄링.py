import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

pq = []
charge = set()

for i in range(k):
    heapq.heappush(pq, (i, arr[i]))

while len(charge) < n and pq:
    num = heapq.heappop(pq)[1]
    charge.add(num)    

cnt = 0
while pq:
    temp = set()

    for i in range(n):
        if pq:
            num = heapq.heappop(pq)[1]
            
            if num not in charge and num not in temp:
                cnt += 1
            
    