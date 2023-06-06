import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N)]

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

cnt = 1
flag = False
for _ in range(M):
    a, b = map(int, input().split())
    
    if find(a) == find(b):
        flag = True
    elif not flag:
        union(a, b)
        cnt += 1
        
if flag:
    print(cnt)
else:
    print(0)