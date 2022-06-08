n = int(input())
arr = list()


for _ in range(n):
    arr.append(int(input()))

answer = 0
index = 0
while True:
    if index + 1 < len(arr):
        if arr[index] >= arr[index + 1]:
            arr[index] = arr[index] - 1
            answer += 1
            index = 0
        else:
            index += 1
    else:
        break
print(answer)