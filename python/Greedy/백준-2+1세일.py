N = int(input())
arr = list()

for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
answer = 0

cnt = 1
temp = 0

for i in range(0, len(arr)):
    if cnt == 3:
        answer += temp
        temp = 0
        cnt = 1
    else:
        temp += arr[i]
        cnt += 1    

answer += temp

print(answer)