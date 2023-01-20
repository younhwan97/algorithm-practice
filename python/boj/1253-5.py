import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(N):
    tmp = arr[:i] + arr[i + 1:]
    start, end = 0, len(tmp) - 1

    while start < end:
        total = tmp[start] + tmp[end]

        if total == arr[i]:
            ans += 1
            break
        elif total > arr[i]:
            end -= 1
        else:
            start += 1
print(ans)