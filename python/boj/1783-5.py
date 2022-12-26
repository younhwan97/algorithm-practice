import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    if m >= 7 and n >= 3:
        ans = 5 + (m - 7) # m - 2
    else:
        if n >= 3:
            ans = m
        elif n == 1:
            ans = 1
        else:
            ans = m // 2 + m % 2

        if ans >= 5:
            ans = 4

    print(ans)

solve() 