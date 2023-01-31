import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * (100_001)
l, r = 0, 0
ans = 1

# 투 포인터라고 해서 반드시 l, r = 0, n - 1로 시작 할 필요는 없다.

while r < n:
    if cnt[arr[r]] < k:
        cnt[arr[r]] += 1
        r += 1
    else:
        cnt[arr[l]] -= 1
        l += 1

    ans = max(ans, r - l)

print(ans)