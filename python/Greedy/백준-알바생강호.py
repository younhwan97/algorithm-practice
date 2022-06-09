import sys

N = int(input())
arr = list()

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

answer = 0

for i in range(0, len(arr)):
    temp = (arr[i] - (i + 1 - 1))
    if temp > 0:
        answer += temp

print(answer) 