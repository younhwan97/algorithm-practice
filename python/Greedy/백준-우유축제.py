N = int(input())
arr = list(map(int, input().split()))

milk_num = 0
answer = 0

for i in range(0, len(arr)):
    if arr[i] == milk_num:
        milk_num += 1
        answer += 1
        if milk_num == 3:
            milk_num = 0

print(answer)