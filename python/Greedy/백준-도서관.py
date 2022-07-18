N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr_minus = list()
arr_plus = list()

for i in range(0, len(arr)):
    if arr[i] > 0:
        arr_plus.append(arr[i])
    else:
        arr_minus.append(arr[i])

answer = 0

index = 0
while arr_minus:
    for i in range(0, M):
        if arr_minus:
            if i == 0:
                temp = -1 * arr_minus[index] * 2
                answer += temp
            del arr_minus[index]
        else:
            break

index = 0
arr_plus.sort(reverse=True)
while arr_plus:
    for i in range(0, M):
        if arr_plus:
            if i == 0:
                temp = arr_plus[index] * 2
                answer += temp
            del arr_plus[index]
        else:
            break

if abs(min(arr)) > abs(max(arr)):
    answer -= abs(min(arr))
else:
    answer -= abs(max(arr))

print(answer)
