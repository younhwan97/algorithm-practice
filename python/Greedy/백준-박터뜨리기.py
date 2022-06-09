N, K = map(int, input().split())

count_arr = [0] * K

for i in range(0, len(count_arr)):
    count_arr[i] += 1
    N -= 1

index = 0
while True:
    if N == 0:
        break
    else:
        if index + 1 < K:
            if count_arr[index] > count_arr[index + 1]:
                index += 1
            else:
                 N -= 1
                 count_arr[index] += 1
        else:
            index = 0

answer = 0

for i in range(0, len(count_arr)):
    if i + 1 < len(count_arr) and count_arr[i] == count_arr[i + 1]:
        answer = -1
        break

if answer == -1:
    print(answer)
else:
    print(max(count_arr) - min(count_arr))