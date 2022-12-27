import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()

    ans = arr[0][0] + arr[0][1]

    for i in range(1, len(arr)):
        if arr[i][0] > ans:
            ans = arr[i][0] + arr[i][1]
        else:
            ans += arr[i][1]
    
    print(ans)
    
solve()