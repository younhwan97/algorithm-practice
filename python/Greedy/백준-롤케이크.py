n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_1 = list()
arr_2 = list()


arr.sort()
for i in range(0, len(arr)):
    if arr[i] % 10 == 0:
        arr_2.append(arr[i])
    else:
        arr_1.append(arr[i])

index = 0
while True:
    if m == 0 or index == len(arr_2):
        break
    else:
        if arr_2[index] <= 10:
            index += 1
        elif arr_2[index] > 10:
            arr_2[index] -= 10
            arr_2.append(10)
            arr_2.sort()
            m -= 1
            index = 0

index = 0
while True:
    if m == 0 or index == len(arr_1):
        break
    else:
        if arr_1[index] <= 10:
            index += 1
        elif arr_1[index] > 10:
            arr_1[index] -= 10
            arr_1.append(10)
            arr_1.sort()
            m -= 1
            index = 0
    
arr_3 = arr_2 + arr_1

answer = 0
for i in range(0, len(arr_3)):
    if arr_3[i] == 10:
        answer += 1

print(answer)