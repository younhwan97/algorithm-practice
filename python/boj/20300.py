import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    
    ans = 0
    if n % 2 != 0:
        ans = arr[-1]

        for i in range(0, n // 2):
            ans = max(ans, arr[i] + arr[len(arr) - 2 - i])
    else:
        for i in range(0, n // 2):
            ans = max(ans, arr[i] + arr[len(arr) - 1 - i])

    print(ans)

solve()