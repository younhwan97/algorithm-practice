import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * 16
arr[0] = 2
arr[1] = 3
arr[2] = 5

for i in range(3, 16):
    arr[i] = arr[i - 1] * 2 - 1

print(arr[N] * arr[N])