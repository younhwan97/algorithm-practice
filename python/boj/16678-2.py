import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(int(input()))

    arr.sort()

    ans = 0
    for i in range(n):
        if i + 1 < n:
            if arr[i] == arr[i + 1]:
                pass
            elif (arr[i] + 1 != arr[i + 1]):
                gap = arr[i + 1] - (arr[i] + 1)
                ans += gap
                arr[i + 1] = arr[i] + 1

    for i in range(n):
        if arr[i] - (i + 1) > 0:
            ans += arr[i] - (i + 1)
            
    print(ans)

solve()