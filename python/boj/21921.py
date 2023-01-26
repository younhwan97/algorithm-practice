import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

now = sum(arr[0: x])
ans = sum(arr[0: x])
cnt = 1

# 슬라이싱 합도 결국 이중 반복문과 같음

for i in range(x, n):
    now = now - arr[i - x] + arr[i]

    if now > ans:
        ans = now
        cnt = 1
    elif now == ans:
        cnt += 1

if ans == 0:
    print("SAD")
else:
    print(ans)
    print(cnt) 