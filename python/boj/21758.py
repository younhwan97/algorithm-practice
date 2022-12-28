import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # 벌통을 왼쪽에
    dp1 = [0] * len(arr)
    dp1[0] = arr[0]

    for i in range(1, len(arr)):
        dp1[i] = dp1[i - 1] + arr[i]

    ans = 2 * dp1[len(dp1) - 3]

    for i in range(len(arr) - 3, -1, -1):
        if i - 1 >= 0:
            tmp = dp1[len(dp1) - 2] - (dp1[i] - dp1[i - 1]) + dp1[i - 1]
            ans = max(ans, tmp)

    # 벌통을 오른쪽에
    dp2 = [0] * len(arr)
    dp2[-1] = arr[-1]

    for i in range(len(arr) - 2, -1, -1):
        dp2[i] = dp2[i + 1] + arr[i]

    ans = max(ans, 2 * dp2[2])

    for i in range(2, len(arr)):
        if i + 1 < len(arr):
            tmp = dp2[1] - (dp2[i] - dp2[i + 1]) + dp2[i + 1]
            ans = max(ans, tmp)

    # 벌통을 가운데
    if n % 2 != 0:
        point = n // 2
        tmp = sum(arr[1:point + 1]) + sum(arr[point: len(arr) - 1])

        ans = max(ans, tmp)
    else:
        point = n // 2

        tmp = sum(arr[1:point + 1]) + sum(arr[point: len(arr) - 1])

        ans = max(ans, tmp)

        point = n // 2 - 1
        
        tmp = sum(arr[1:point + 1]) + sum(arr[point: len(arr) - 1])

        ans = max(ans, tmp)

    print(ans)

solve()