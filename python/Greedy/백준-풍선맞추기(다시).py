import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

hit_status = [0] * (1_000_001)
cnt = 0
for i in range(n):
    if hit_status[arr[i]] == 0:
        hit_status[arr[i] - 1] += 1
        cnt += 1
    else:
        hit_status[arr[i]] -= 1
        hit_status[arr[i] - 1] += 1

print(cnt)