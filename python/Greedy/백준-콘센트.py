import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

pq = []

for i in range(n):
    if len(pq) < m:
        heapq.heappush(pq, arr[i])
    else:
        value = heapq.heappop(pq)
        heapq.heappush(pq, value + arr[i])

print(max(pq))