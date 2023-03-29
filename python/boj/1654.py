import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))

end = max(arr)
start = 1
ans = 0
while end >= start:
    mid = (end + start) // 2

    cnt = 0
    for value in arr:
        cnt += (value // mid)

    if cnt >= N:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)

# K, N = map(int, input().split())
# arr = list()
# for _ in range(K):
#     arr.append(int(input()))

# left = 1
# right = max(arr)
# result = 0
# while right >= left:
#     mid = (left + right) // 2

#     cnt = 0
#     for value in arr:
#         cnt += (value // mid)

#     if cnt < N:
#         right = mid - 1
#     elif cnt >= N:
#         result = mid
#         left = mid + 1
# print(result)