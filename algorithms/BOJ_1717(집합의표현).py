import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(M):
    a, b, c = map(int, input().split())
    
    if a == 0:
        union(b, c)
    else:
        x, y = find(b), find(c)
        if x != y:
            print("NO")
        else:
            print("YES")