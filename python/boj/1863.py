import sys
input = sys.stdin.readline

N = int(input())
arr = []

ans = 0
for _ in range(N):
    a, b = map(int, input().split())

    while arr and arr[-1] > b:
        arr.pop()
        
    if arr and arr[-1] == b:
        pass
    else:
        if b != 0:
            ans += 1
            arr.append(b)
print(ans)

# N = int(input())
# arr = list()
# for _ in range(N):
#     a, b = map(int, input().split())
#     arr.append((a, b))

# check = set()
# ans = 0
# minimum_height = 0

# for i in range(len(arr)):
#     x, y = arr[i]

#     if y > minimum_height:
#         ans += 1
#         check.add(y)
#     elif y == 0:
#         check.clear()
#     elif y < minimum_height:
#         if y not in check:
#             ans += 1
#             check.add(y)

#         new_check = set()
#         while check:
#             tmp = check.pop()

#             if tmp <= y:
#                 new_check.add(tmp)
#         check = new_check
    
#     minimum_height = y
# print(ans)