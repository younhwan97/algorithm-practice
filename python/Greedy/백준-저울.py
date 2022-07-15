N = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum = arr[0]

if sum > 1:
    ## 무게가 1인 추가 없을 때
    print(1)
else:
    ## 1 1 1 1 20 30 40 -> 5
    for i in range(1, len(arr)):
        if sum < arr[i] and sum + 1 != arr[i]:
            break
        else:
            sum += arr[i]

    print(sum + 1)