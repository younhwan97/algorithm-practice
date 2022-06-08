N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

answer = 0
attach_point = 0

for index in range(0, len(arr)):
    if attach_point == 0 or attach_point + L < arr[index]:
        answer += 1
        attach_point = arr[index] - 0.5

print(answer)