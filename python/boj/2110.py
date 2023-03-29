import sys
input = sys.stdin.readline

N, C = map(int, input().split())
# N, C <= 200,000 
# x < 1,000,000,000
arr = list()
for _ in range(N):
    x = int(input())
    arr.append(x)