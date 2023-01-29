import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    
    left_top = -1
    for j in range(0, i):
        left_top = max(left_top, arr[j])

    right_top = -1
    for j in range(i + 1, w):
        right_top = max(right_top, arr[j])

    if left_top > arr[i] and right_top > arr[i]:
        ans += (min(left_top, right_top) - arr[i])
print(ans)