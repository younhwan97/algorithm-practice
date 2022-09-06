import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = input().strip()
max_value = max(arr[:k + 1])
index = arr.index(max_value)

answer = deque()
answer.append(max_value)
k -= index

for i in range(index + 1, len(arr)):
    if i + 1 < len(arr):
        if arr[i] > arr[i + 1]:
            answer.append(arr[i])
        else:
            if k <= 0:
                answer.append(arr[i])
            else:
                k -= 1
    else:
        answer.append(arr[i])

while k > 0:
    answer.pop()
    k -= 1

while answer:
    print(answer.popleft(), end="")