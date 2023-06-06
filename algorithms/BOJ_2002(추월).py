import sys
input = sys.stdin.readline

N = int(input())
start, end = dict(), []

num = 1
for _ in range(N):
    start[input().strip()] = num
    num += 1

for _ in range(N):
    end.append(input().strip())

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if start[end[i]] > start[end[j]]:
            ans += 1
            break
print(ans)