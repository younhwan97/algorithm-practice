import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = [0] * (n + 1)

pq = []

for i in range(n):
    heapq.heappush(pq, arr[i])

while pq:
    value = heapq.heappop(pq)

    if value < n + 1:
        if result[value] == 0:
            result[value] = 1
        else:
            heapq.heappush(pq, value + k)
    else:
        break

result[0] = 1

if min(result) == 1 and max(result) == 1:
    print(1)
else:
    print(0)