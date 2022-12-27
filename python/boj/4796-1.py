import sys
input = sys.stdin.readline

def solve():
    num = 1
    while True:
        a, b, c = map(int, input().split())

        if a == 0 and b == 0 and c == 0:
            break

        ans = (c // b) * a + min(a, c % b)
            
        print("Case " + str(num)+": " + str(ans))
        num += 1

solve()