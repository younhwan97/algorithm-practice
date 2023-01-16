import sys, heapq
input = sys.stdin.readline

W, N = map(int, input().split())

pq = []
for _ in range(N):
    weight, price = map(int, input().split())
    heapq.heappush(pq, (-1 * price, -1 * weight))

ans = 0 

while pq and W > 0:
    price, weight = heapq.heappop(pq)
    price, weight = -1 * price, -1 * weight

    if W >= weight:
        ans += (price) * weight
        W -= weight
    else:
        ans += (price) * W
        W = 0

print(ans)