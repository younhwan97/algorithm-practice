import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
dp = [[0] * 2001 for _ in range(2001)]

