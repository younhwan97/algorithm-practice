import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] * 101
height = 1
for _ in range(N):
    a, b = map(int, input().split())
  
    for j in range(height, height + a):
        arr[j] = b
    height += a

ans = 0
height = 1
for _ in range(M):
    a, b = map(int, input().split())

    for j in range(height, height + a):
        ans = max(ans, b - arr[j])
    height += a

print(ans)