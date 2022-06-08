N = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

answer = 1

for index in range(0, len(arr)):
    if index == 0:
        answer = answer + 1 + arr[index]
    else:
        temp = 1 + index + 1 + arr[index]
        if temp > answer:
            answer = temp

print(answer)