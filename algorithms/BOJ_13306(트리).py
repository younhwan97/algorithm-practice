## 수정 필요
## 43/100점
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)

N, Q = map(int, input().split())
parent = [-1] + [i + 1 for i in range(N)]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if x != parent[x]:
        return find(parent[x])
    return x

for i in range(N - 1):
    p = int(input())
    c = i + 2
    parent[c] = p

ans = []
for _ in range(N - 1 + Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        # 제거
        a = tmp[1]
        parent[a] = a
    else:
        # 질의
        a, b = tmp[1], tmp[2]
        if find(a) == find(b):
            ans.append("YES")
        else:
            ans.append("NO")

for a in ans:
    print(a)