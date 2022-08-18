import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list()
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    if n == 1:
        print(max(map(max, arr)))
    else:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

        for i in range(2, n):
            arr[0][i] += max(max(arr[0][i - 2], arr[1][i - 2]), arr[1][i - 1])

            arr[1][i] += max(arr[0][i - 1], max(arr[1][i - 2], arr[0][i - 2]))

        print(max(map(max, arr)))