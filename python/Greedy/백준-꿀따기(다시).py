def getAnswer(arr):
    answer = 0
    loss = 0
    second_index = 0

    for i in range(0, len(arr)):
    ## 첫 번째 인덱스에 첫 번째 벌들을 위치시킨다.
        if i != 0:
            ## 현재 인덱스에 두 번째 벌들을 위치시켰을 때 발생할 수 있는 손해를 계산한다.
            if i == 1:
                loss = arr[1] * 2
                second_index = 1
            else:
                temp = 0
                for j in range(1, i):
                    temp += arr[j]

                temp += (arr[i] * 2)
            
                if temp < loss:
                    loss = temp
                    second_index = i

    for i in range(1, len(arr)):
        if i != second_index:
            answer += arr[i]        

    for i in range(second_index + 1, len(arr)):
        answer += arr[i]

    return answer

N = int(input())
arr = list(map(int, input().split()))
answer = list()

## 벌통을 오른쪽 끝에 두는 경우
answer.append(getAnswer(arr))

## 벌통을 왼쪽 끝에 두는 경우
answer.append(getAnswer(list(reversed(arr))))

## 벌통을 가운데 두는 경우
temp = 0
temp_index = len(arr) // 2
for i in range(1, len(arr) - 1):
    temp += arr[i]
temp += arr[temp_index]
answer.append(temp)

temp = 0
temp_index = len(arr) // 2 + 1
for i in range(1, len(arr) - 1):
    temp += arr[i]
temp += arr[temp_index]
answer.append(temp)

print(max(answer))