import sys

N, M = map(int, input().split())

arr = []
for _ in range(N):
    w, p = map(int, sys.stdin.readline().split())
    arr.append((p, w))

arr.sort(reverse=True)
cal_arr = [0] * N

for i in range(N):
    sum_weight = arr[i][1]

    for j in range(i + 1, N):
        if arr[j][0] < arr[i][0]:
            sum_weight += arr[j][1]

    cal_arr[i] = (arr[i][0], sum_weight)

min_price = cal_arr[0][0]
for i in range(len(cal_arr)):
    if M <= cal_arr[i][1]:
        if min_price > cal_arr[i][0]:
            min_price = cal_arr[i][0]
    else:
        break
