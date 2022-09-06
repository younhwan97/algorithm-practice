import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[] for _ in range(1001)] 

for i in range(n):
    temp = []

    for j in range(i):
        if len(dp[i]) == 0:
            if arr[i] > arr[j]:
                dp[i].append(arr[j])
                temp.append(arr[j])
        else:
            if dp[i][len(dp[i]) - 1] < arr[j] and arr[i] > arr[j]:
                dp[i].append(arr[j])
            elif dp[i][len(dp[i]) - 1] > arr[j] and arr[i] > arr[j]:
                temp.append(arr[j])

    if len(dp[i]) < len(temp):
        dp[i] = temp.copy()

    dp[i].append(arr[i])

max_length = 0

for i in range(n):
    if len(dp[i]) > max_length:
        max_length = len(dp[i])

for i in range(n):
    if len(dp[i]) == max_length:
        print(max_length)

        for j in range(max_length):
            print(dp[i][j], end=' ')

        break