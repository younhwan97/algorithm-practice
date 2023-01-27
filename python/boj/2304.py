import sys
input = sys.stdin.readline

N = int(input())
arr = list()
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

max_height = arr[0][1]
for i in range(N): max_height = max(max_height, arr[i][1])

ans = 0
l_index = 0
while arr[l_index][1] != max_height:
    height = arr[l_index][1]
    
    for i in range(l_index + 1, N):
        if arr[i][1] > height:
            ans += (arr[i][0] - arr[l_index][0]) * height
            l_index = i
            break

r_index = N - 1
while arr[r_index][1] != max_height:
    height = arr[r_index][1]

    for i in range(r_index - 1, -1 , -1):
        if arr[i][1] > height:
            ans += (arr[r_index][0] - arr[i][0]) * height
            r_index = i
            break

ans += (arr[r_index][0] - arr[l_index][0] + 1) * max_height
print(ans)