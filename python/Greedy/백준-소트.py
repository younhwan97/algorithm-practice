import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

sorted_arr = sorted(arr, reverse=True)

point = 0
for i in range(len(sorted_arr)):
    if arr == sorted_arr or s <= 0:
        break

    idx = arr.index(sorted_arr[i])
    
    if idx >= point and s - (idx - point) >= 0:
        s = s - (idx - point)
        temp = arr[idx]
        arr.remove(temp)
        arr.insert(point, temp)
        point += 1

print(' '.join(map(str, arr)))