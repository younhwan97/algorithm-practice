import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
line = [-1] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == arr[i] and line[j] == -1:
            line[j] = i + 1
            break

        if line[j] == -1:
            cnt += 1