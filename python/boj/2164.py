import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque([i + 1 for i in range(N)])

while len(arr) > 1:
    arr.popleft()
    tmp = arr.popleft()
    arr.append(tmp)

print(arr.pop())

# while len(arr) != 1:
#     tmp = list()

#     for i in range(len(arr)):
#         if i % 2 != 0:
#             tmp.append(arr[i])
    
#     if len(arr) % 2 != 0:
#         tmp = tmp[1:] + [tmp[0]]
    
#     arr = tmp
# print(arr[0])