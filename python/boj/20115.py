import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    ans = arr[-1]

    for i in range(N - 1):
        ans += arr[i] / 2

    if ans == int(ans):
        print(int(ans))
    else:
        print(ans)
    
solve()