N = int(input())
arr_1 = list(input())
arr_2 = list(input())
temp = arr_1.copy()

def click_switch(value):
    if value == '0' or value == 0:
        return '1'
    else:
        return '0'

## 첫 번째 전구의 스위치를 누르지 않은 경우
answer_1 = 0
for i in range(N):
    if i + 2 < N:
        if arr_1[i] != arr_2[i]:
            arr_1[i + 1] = click_switch(arr_1[i + 1])
            arr_1[i] = click_switch(arr_1[i])
            arr_1[i + 2] = click_switch(arr_1[i + 2])
            answer_1 += 1
    elif i + 2 == N:
        if arr_1[i] != arr_2[i]:
            arr_1[i + 1] = click_switch(arr_1[i + 1])
            arr_1[i] = click_switch(arr_1[i])
            answer_1 += 1

if arr_1 == arr_2:
    print(answer_1)
else:
    ## 첫 번째 전구의 스위치를 누른 경우
    answer_2 = 1
    arr_1 = temp.copy()
    arr_1[0] = click_switch(arr_1[0])
    arr_1[1] = click_switch(arr_1[1])
    for i in range(N):
        if i + 2 < N:
            if arr_1[i] != arr_2[i]:
                arr_1[i + 1] = click_switch(arr_1[i + 1])
                arr_1[i] = click_switch(arr_1[i])
                arr_1[i + 2] = click_switch(arr_1[i + 2])
                answer_2 += 1
        elif i + 2 == N:
            if arr_1[i] != arr_2[i]:
                arr_1[i + 1] = click_switch(arr_1[i + 1])
                arr_1[i] = click_switch(arr_1[i])
                answer_2 += 1

    if arr_1 == arr_2:
        print(answer_2)
    else:
        print(-1)