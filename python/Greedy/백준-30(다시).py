arr = list(input())
arr = list(map(int, arr))

# 30(10x3)의 배수가 되는 조건
## 1. 일의 자리수가 0
## 2. 각 자리수의 합이 3의 배수

arr.sort(reverse=True)

if sum(arr) % 3 != 0 or arr[len(arr) - 1] != 0:
    print(-1)
else:
    answer = ""
    for i in range(0, len(arr)):
        answer += str(arr[i])
    print(answer)