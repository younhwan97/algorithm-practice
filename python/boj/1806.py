import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = n - 1
ans = sum(arr)

while left + 1< right and ans > s:
    if arr[left] < arr[right]:
        if ans - arr[left] >= s:
            ans -= arr[left]
            left += 1
        elif ans - arr[right] >= s:
            arr -= arr[right]
            right -= 1
        else:
            break
    else:
        if ans - arr[right] >= s:
            ans -= arr[right]
            right -= 1
        elif ans - arr[left] >= s:
            ans -= arr[left]
            left += 1
        else:
            break

if ans < s:
    print(ans)
else:
    print(right - left + 1)