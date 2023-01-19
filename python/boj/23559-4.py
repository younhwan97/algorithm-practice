import sys, heapq
input = sys.stdin.readline

N, X = map(int, input().split())
pq = []
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    if B >= A:
        # 1000원짜리 메뉴가 더 맛있는 경우
        X -= 1000
        ans += B
    else:
        # 5000원짜리 메뉴가 더 맛있는 경우
        heapq.heappush(pq, (-1 * abs(A - B), -1 * A, B))

while pq:
    gap, a, b = heapq.heappop(pq)
    a *= -1

    if X >= 5000 and (X - 5000) >= len(pq) * 1000:
        X -= 5000
        ans += a
    else:
        X -= 1000   
        ans += b

print(ans)