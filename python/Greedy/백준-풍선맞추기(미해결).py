N = int(input())
arr = list(map(int, input().split()))

answer = []
answer.append(arr[0])

## 2 1 5 4 3
for i in range(1, len(arr)):
    pass_validation_check = False

    for j in range(0, len(answer)):
        if arr[i] + 1 == answer[j]:
            answer[j] = arr[i]
            pass_validation_check = True
            break
    
    if pass_validation_check == False:
        answer.append(arr[i])

print(len(answer))