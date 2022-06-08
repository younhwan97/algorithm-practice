import sys

N = int(input())

arr = list()

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

rank = 1

answer = 0

for i in range(0, len(arr)):
    temp = arr[i]
    answer += abs(rank - temp)
    rank += 1

print(answer)