import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

index = (len(arr) - 1) // 2

print(arr[index])