import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = list()
for _ in range(N): arr.append(int(input()))

arr = arr * 2
ans = 0
for i in range(N):
    tmp = arr[i: i + k]
    tmp = set(tmp)
    tmp.add(c)
    ans = max(ans, len(tmp))
print(ans)