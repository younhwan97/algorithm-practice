import sys

input = sys.stdin.readline

n = int(input())

arr = list()

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

