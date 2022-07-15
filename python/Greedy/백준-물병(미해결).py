N, K = map(int, input().split())

arr = [1] * N

answer = 0

while True:
    if len(arr) == K:
        break
    else:
        pass_validation_check = False

        for i in range(0, len(arr)):
            if i + 1 < len(arr) and arr[i] == arr[i + 1]:
                arr[i] = arr[i] * 2
                del arr[i + 1]
                pass_validation_check = True
                break
        
        if pass_validation_check == False:
            arr.append(1)
            answer += 1
            
print(answer)