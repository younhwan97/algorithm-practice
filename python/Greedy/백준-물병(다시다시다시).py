import sys

## 입력
input = sys.stdin.readline

N, K = map(int, input().split())

def check(num):
    ans = 0

    while True:
        a = num // 2
        b = num % 2
        ans += b
        num = a

        if num == 0:
            return ans

if K >= N:
    print(0)
else:
    i = N
    while True:
        if check(i) <= K:
            print(i - N)
            break
        else:
            i += 1