import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

sorted_arr = sorted(arr, reverse=True)
result = list()
target_position = 0

for i in range(n):
    value = sorted_arr[i]
    index = arr.index(value)

    if 0 < abs(index - target_position) <= k:
        arr.remove(value)
        arr.insert(target_position, value)
        k -= (index - target_position)
        target_position += 1
    elif abs(index - target_position) == 0:
        target_position += 1
    
    if k == 0:
        break

for i in range(len(arr)):
    if i + 1 < len(arr):
        print(arr[i], end=' ')
    else:
        print(arr[i])