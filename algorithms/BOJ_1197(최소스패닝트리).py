import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
pq = []
for _ in range(E):
    s, e, c = map(int, input().split())
    heapq.heappush(pq, (c, s, e))

# 부모 테이블 초기화
parent = [0] * (V + 1) 
for i in range(1, V+ 1):
    parent[i] = i

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
while pq:
    c, s, e = heapq.heappop(pq)

    if find(s) != find(e):
        union(s, e)
        ans += c

print(ans)