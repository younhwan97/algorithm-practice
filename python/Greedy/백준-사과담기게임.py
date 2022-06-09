N, M = map(int, input().split())
j = int(input())
arr = list()

for _ in range(j):
    arr.append(int(input()))

position = [1, M]

answer = 0

i = 0
while True:
    if i == len(arr):
        break

    if position[0] <= arr[i] and position[1] >= arr[i]:
        i += 1
    else:
        answer += 1
        if position[0] >= arr[i]:
            position[0] -= 1
            position[1] -= 1
        elif position[1] <= arr[i]:
            position[0] += 1
            position[1] += 1

print(answer)