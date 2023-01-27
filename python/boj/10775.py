import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

l_index = 0
r_index = n - 1
ans = abs(arr[l_index] + arr[r_index])

l_value = arr[0]
r_value = arr[n - 1]

while l_index + 1 < r_index:
    if abs(arr[r_index]) > abs(arr[l_index]):
        r_index -= 1
    elif abs(arr[r_index]) < abs(arr[l_index]):
        l_index += 1
    else:
        break
    
    if abs(arr[l_index] + arr[r_index]) < ans:
        l_value = arr[l_index]
        r_value = arr[r_index]
        ans = abs(arr[l_index] + arr[r_index])

print(l_value, r_value)