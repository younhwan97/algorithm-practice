import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    arr = []

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, -1 * b))

    arr.sort(reverse=True)
    ans = 0

    for a, b in arr:
        if k < 0:
            break

        b = -1 * b

        if a > b and k >= 5000:
            k -= 5000
            ans += a
        elif k >= 1000:
            k -= 1000
            ans += b

    print(ans)
    
solve()