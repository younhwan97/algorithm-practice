import sys

N, M = map(int, input().split())
arr = list()

for _ in range(N):
    weight, price = map(int, sys.stdin.readline().split())
    arr.append([price, weight])

arr.sort(reverse=True)

## 가격이 제일 비싼 고기를 샀을 때
answer = arr[0][0]

for i in range(1, len(arr)):
    weight = 0

    for j in range(i + 1, len(arr)):
        if arr[i][0] > arr[j][0]:
            weight += arr[j][1]

            if weight >= M:
                break

    if weight >= M:
        answer = arr[i][0]
print(answer)