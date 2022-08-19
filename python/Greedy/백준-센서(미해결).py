import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr)