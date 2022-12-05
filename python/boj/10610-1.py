import sys
input = sys.stdin.readline

# 30(10x3)의 배수가 되는 조건
## 1. 일의 자리수가 0
## 2. 각 자리수의 합이 3의 배수 ex) 102의 경우 1 + 0 + 2 (= 3)이 3의 배수이기 때문에 패스

def solve():
    num = list(map(int, input().strip()))
    num.sort(reverse=True)

    if sum(num) % 3 != 0 or num[-1] != 0:
        print(-1)
    else:
        ans = ""

        for n in num:
            ans += str(n)

        print(int(ans))

solve()