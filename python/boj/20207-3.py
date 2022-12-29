import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = []

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, -1 * b))

    arr.sort()

    floor = [0] * 1002
    start = -1
    last = -1

    ans = 0
    for s, e in arr:
        e = -1 * e

        if s > last + 1:
            height = -1

            for i in range(1, 1002):
                if floor[i] == 0:
                    height = i - 1
                    break
                else:
                    floor[i] = 0

            ans += ((last - start + 1) * height)
            last = -1
            start = -1

        for i in range(1, 1001):
            if floor[i] < s:
                floor[i] = e
                last = max(last, e)

                if start == -1:
                    start = s

                break

    height = -1
    for i in range(1, 1002):
        if floor[i] == 0:
            height = i - 1
            break
    
    ans += ((last - start + 1) * height)

    print(ans)
    
solve()